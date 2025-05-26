/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ActionpadWidget } from "@point_of_sale/app/screens/product_screen/action_pad/action_pad";
import { _t } from "@web/core/l10n/translation";

patch(ActionpadWidget.prototype, {
    async onClickHello() {
        console.log("Hello button clicked");
    },
});

