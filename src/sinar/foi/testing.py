# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sinar.foi


class SinarFoiLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=sinar.foi)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sinar.foi:default')


SINAR_FOI_FIXTURE = SinarFoiLayer()


SINAR_FOI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SINAR_FOI_FIXTURE,),
    name='SinarFoiLayer:IntegrationTesting',
)


SINAR_FOI_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SINAR_FOI_FIXTURE,),
    name='SinarFoiLayer:FunctionalTesting',
)


SINAR_FOI_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SINAR_FOI_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SinarFoiLayer:AcceptanceTesting',
)
