// import { Component, useState } from "@odoo/owl";
// import { usePos } from "@point_of_sale/app/store/pos_hook";
// import { useService } from "@web/core/utils/hooks";

// export class SelectPartnerButton extends Component {
//     static template = "point_of_sale.SelectPartnerButton";
//     static props = ["partner?"];
//     setup() {
//         this.pos = usePos();
//         this.ui = useState(useService("ui"));
//     }
// }

// odoo.define("custom_discount_button.DiscountButton",function (require) {
//     "use strict";
//     const PosComponent = require("point_of_sale.PosComponent");
//     const ProductScreen = require("point_of_sale.ProductScreen");
//     const Registries = require("point_of_sale.Registries");

//     class DiscountButton extends PosComponent{

//     }

//     DiscountButton.template = "DiscountButton";

//     ProductScreen.addControllButton({
//         component: DiscountButton,
//         position: ["before", "point_of_sale.SelectPartnerButton"],
//     })

//     Registries.Component.add(DiscountButton);

//     return DiscountButton;

// })

// Corrected discount_button.js
odoo.define("custom_discount_button.DiscountButton", function(require) {
    "use strict";

    const { useListener } = require("@web/core/utils/hooks");
    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");

    class DiscountButton extends PosComponent {
        setup() {
            super.setup();
            useListener('click-discount', this.onClick);
        }

        async onClick() {
            const order = this.env.pos.get_order();
            if (order && order.selected_orderline) {
                order.selected_orderline.set_discount(10); // 10% discount
                order.trigger('change');
            }
        }
    }

    DiscountButton.template = "DiscountButton";

    ProductScreen.addControlButton({
        component: DiscountButton,
        position: ["after", "OrderlineCustomerNoteButton"],
    });

    Registries.Component.add(DiscountButton);

    return DiscountButton;
});