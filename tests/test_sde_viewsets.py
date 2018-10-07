# -*- coding: utf-8 -*-
import os
import inspect
from django.db import models
from django.test import TestCase
from django.test.utils import captured_stdout
from django.core.management import call_command
from armada_sde import models as sde_models


class LoadSDEModelsTests(TestCase):
    def setUp(self):
        self._settings = os.environ.get('DJANGO_SETTINGS_MODULE')
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

    def tearDown(self):
        if self._settings:
            os.environ['DJANGO_SETTINGS_MODULE'] = self._settings

    def test_sde_model_listing(self):
        with captured_stdout() as stdout:
            call_command('generate_viewsets')
        output = stdout.getvalue()
        for name in dir(sde_models):
            sde_class = getattr(sde_models, name)
            if inspect.isclass(sde_class) and issubclass(sde_class,
                                                         models.Model):
                self.assertIn('class {}ViewSet(SDEViewSet)'.format(name),
                              output,
                              msg='{} viewset missing'.format(name))

                self.assertIn('class {}ListSerializer'.format(name),
                              output,
                              msg='{} list serializer missing'.format(name))

                self.assertIn('class {}DetailsSerializer'.format(name),
                              output,
                              msg='{} details serializer missing'.format(name))

                self.assertIn('views.{}ViewSet'.format(name),
                              output,
                              msg='{} routing missing'.format(name))

