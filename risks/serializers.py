from rest_framework import serializers
from .models import RiskType, RiskField, RiskFieldOption


class RiskFieldOptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = RiskFieldOption
		fields = ('name',)


class RiskFieldSerializer(serializers.ModelSerializer):
	options = RiskFieldOptionSerializer(many=True, required=False)

	class Meta:
		model = RiskField
		fields = (
			'risk', 'name', 'field_type', 'is_required', 'options',
		)
		read_only_fields = ('risk', )


class RiskTypeSerializer(serializers.ModelSerializer):
	fields = RiskFieldSerializer(many=True)

	class Meta:
		model = RiskType
		fields = (
			'pk', 'name', 'slug', 'fields',
		)
		read_only_fields = ('slug', )

	def create(self, validated_data):
		fields_data = validated_data.pop('fields')
		risk = RiskType.objects.create(**validated_data)

		for field_data in fields_data:
			options = []
			if 'options' in field_data and field_data.get('field_type') == 'enum':
				options = field_data.get('options') 
				del field_data['options']

			risk_field = RiskField.objects.create(risk=risk, **field_data)

			for option in options:
				RiskFieldOption.objects.create(risk_field=risk_field, name=option.get('name'))

		return risk
