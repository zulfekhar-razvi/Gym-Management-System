frappe.pages['gym-member-profile'].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'My Gym Profile',
        single_column: true
    });

    frappe.call({
        method: "frappe.client.get",
        args: {
            doctype: "Gym Member",
            name: frappe.session.user
        },
        callback: function(r) {
            if (!r.message) return;

            let member = r.message;

            let html = `
                <h3>Active Plan</h3>
                <p>${member.active_membership || "No Active Plan"}</p>

                <h3>Trainer</h3>
                <p>${member.active_trainer || "Not Assigned"}</p>

                <h3>Remaining Days</h3>
                <p>Calculated from membership</p>

                <h3>Past Plans</h3>
                <p>History coming from Gym Membership</p>
            `;

            page.main.html(html);
        }
    });
};
