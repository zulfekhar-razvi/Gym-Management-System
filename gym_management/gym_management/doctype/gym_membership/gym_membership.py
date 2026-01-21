import frappe
import unittest

class TestGymMembership(unittest.TestCase):

    def setUp(self):
        self.member = frappe.get_doc({
            "doctype": "Gym Member",
            "member_name": "Test Member"
        }).insert(ignore_permissions=True)

    def test_create_membership(self):
        membership = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": self.member.name,
            "membership_type": "Monthly",
            "start_date": frappe.utils.today(),
            "amount": 1000
        }).insert(ignore_permissions=True)

        self.assertTrue(membership.name)

    def test_submit_membership(self):
        membership = frappe.get_doc({
            "doctype": "Gym Membership",
            "member": self.member.name,
            "membership_type": "Monthly",
            "start_date": frappe.utils.today(),
            "amount": 1000
        }).insert(ignore_permissions=True)

        membership.submit()

        self.assertEqual(membership.docstatus, 1)
