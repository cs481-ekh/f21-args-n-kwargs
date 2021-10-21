from django.test import TestCase

from equipment.forms import EquipmentForm


class EquipmentFormTest(TestCase):
    name = "Rotary Disc cutter",
    model = "Model 360",
    manufacturer = "South Bay",
    pi = "Steve Jobs",
    contact = "Steve Jobs",
    room = "CS1001",
    lab = "BSCMC",
    description = "Cutting 3 mm",
    url = "www.google.com",
    permission = "Student"

    def test_equipment_form_valid(self):
        form = EquipmentForm(data={'name': self.name, 'model': self.model, 'manufacturer': self.manufacturer,
                                   'year': 2016, 'pi': self.pi, 'contact': self.contact,
                                   'room': self.room, 'lab': self.lab, 'description': self.description,
                                   'url': self.url, 'permission': self.permission})
        self.assertTrue(form.is_valid())

    def test_equipment_form_invalid_year_min(self):
        form = EquipmentForm(data={'name': self.name, 'model': self.model, 'manufacturer': self.manufacturer,
                                   'year': 1949, 'pi': self.pi, 'contact': self.contact,
                                   'room': self.room, 'lab': self.lab, 'description': self.description,
                                   'url': self.url, 'permission': self.permission})
        self.assertFalse(form.is_valid())


    def test_equipment_form_invalid_year_max(self):
        form = EquipmentForm(data={'name': self.name, 'model': self.model, 'manufacturer': self.manufacturer,
                                   'year': 3001, 'pi': self.pi, 'contact': self.contact,
                                   'room': self.room, 'lab': self.lab, 'description': self.description,
                                   'url': self.url, 'permission': self.permission})
        self.assertFalse(form.is_valid())

    def test_equipment_form_valid_null_values(self):
        form = EquipmentForm(data={'name': self.name, 'model': self.model, 'manufacturer': self.manufacturer,
                                   'year': 2020, 'pi': self.pi, 'contact': None,
                                   'room': None, 'lab': self.lab, 'description': None,
                                   'url': None, 'permission': self.permission})
        self.assertTrue(form.is_valid())

