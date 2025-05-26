/**@odoo-module **/
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";

patch(ControlButtons.prototype, {
    async onClickHello() {
        this.dialog.add(AlertDialog, {
            title: _t("Greeting"),
            body: _t("Hello from POS!"),
        });
    },
    async onClickPopup() {
        this.dialog.add(AlertDialog, {
            title: _t("Custom Alert"),
            body: _t("Choose the alert type"),
        });
    },

    // New loyalty points method
    async onClickLoyalty() {
        this.dialog.add(AlertDialog, {
            title: _t("Loyalty Points"),
            body: _t("Customer has 150 points"),
        });
    },

    async applyQuickDiscount() {
        const order = this.pos.get_order();
        const orderline = order?.get_selected_orderline();
        if (orderline) {
            orderline.set_discount(10);
            this.render();
        }
    },
});
