from django.test import TestCase
from edc_forms.forms import SmearPositiveTBForm
from model_bakery import baker
from pprint import pprint

# Read about https://model-bakery.readthedocs.io/en/latest/recipes.html
# to generate test data


class SmearPositiveTBTest(TestCase):
    def setUp(self):
        super().setUp()

    def test_smearPositiveTb(self):
        data = {
            'age_15_24': 'frd',
            'age_25_34': 12,
            'age_35_44': 12,
            'age_45_54': 12,
            'age_55_64': 12,
            'age_65_above': 12,
            'gender_male': 12,
            'gender_female': 12,
            'soc_econ_pos_low': 12,
            'soc_econ_pos_middle': 12,
            'soc_econ_pos_high': 12,
        }
        form = SmearPositiveTBForm(data=data)
        form.is_valid()
        self.assertIn('age_15_24', form._errors)

        data.update(age_15_24=1)
        form = SmearPositiveTBForm(data=data)
        form.is_valid()
        print(form._errors)
        self.assertNotIn('age_15_24', form._errors)
