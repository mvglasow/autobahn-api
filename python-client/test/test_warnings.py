"""
    Autobahn App API

    Was passiert auf Deutschlands Bundesstraßen? API für aktuelle Verwaltungsdaten zu Baustellen, Staus und Ladestationen. Außerdem Zugang zu Verkehrsüberwachungskameras und vielen weiteren Datensätzen.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.autobahn.model.warning import Warning

from deutschland import autobahn

globals()["Warning"] = Warning
from deutschland.autobahn.model.warnings import Warnings


class TestWarnings(unittest.TestCase):
    """Warnings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWarnings(self):
        """Test Warnings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Warnings()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
