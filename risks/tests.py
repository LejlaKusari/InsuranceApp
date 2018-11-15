from .models import RiskType, RiskField, RiskFieldOption
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase


class RiskTypeTests(APITestCase):
	def test_list_risk_type(self):
		url = reverse('risk-list')
		for i in range(3):
			RiskType.objects.create(name='RiskTypeName-{}'.format(i+1))
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('count'), 3)

	def test_retrieve_risk_type(self):
		risk_type = RiskType.objects.create(name='RiskTypeName-1')
		url = reverse('risk-detail', kwargs={'pk': risk_type.pk})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data.get('pk'), risk_type.pk)

	def test_create_risk_type(self):
		url = reverse('risk-create')
		data = {
			'name': 'FireInsurance',
			'fields': [
				{
					'name': 'First name',
					'field_type': 'text'
				},
				{
					'name': 'Last name',
					'field_type': 'text'
				},
				{
					'name': 'Age',
					'field_type': 'number'
				},
				{
					'name': 'Date of birth',
					'field_type': 'date',
				},
				{
					'name': 'Gender',
					'field_type': 'enum',
					'options': [
						{ 'name': 'Female' },
						{ 'name': 'Male' }
					]
				}
			]
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		
	def test_create_risk_entry(self):
		risk = RiskType.objects.create(name='Test Insurance type')

		field_types = ['text', 'number', 'date', 'enum']

		for field_type in field_types:
			risk_field = RiskField.objects.create(risk=risk, name='{} test field'.format(field_type), field_type=field_type)

			if field_type == 'enum':
				for i in range(3):
					RiskFieldOption.objects.create(risk_field=risk_field, name='test option #{}'.format(i+1))
		
		url = reverse('risk-entry-create')
		data = {
			'risk_type': risk.id,
			'entry_data': {
				'text test field': { 'value': 'test text input' },
				'number test field': { 'value': 33 },
				'date test field': { 'value': '2018-10-10' },
				'enum test field': { 'value': 'test option #1' }
			}
		}

		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIsNotNone(response.json().get('id'))
