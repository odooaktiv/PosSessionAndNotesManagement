odoo.define('pos_restaurant_customisation.pos_restaurant_customisation', function (require) {
"use strict";
    var models = require('point_of_sale.models');
    var _super_order = models.Order.prototype;
    var _super_orderline = models.Orderline.prototype;

    models.load_models({
        model:  'res.users',
        fields: ['is_cashier', 'is_waiter'],
        loaded: function(self,users){
            for (var i = 0; i < users.length; i++) {
                var user = _.find(self.users, function(el){ return el.id == users[i].id; });
                if (user) {
                    _.extend(user,users[i]);
                }
            }
        }
    });

    models.Order = models.Order.extend({
        export_for_printing: function() {
            var json = _super_order.export_for_printing.apply(this,arguments);
            this.orderlines.each(function(line, index){
                var note = line.get_note();
                json.orderlines[index]['note'] = note;
            });
            return json;
        },

        get_note: function(){
            return this.pos.note;
        },
    });

    //START DISABLE CHANGE CASHIER
    chrome.UsernameWidget.include({
    template: 'UsernameWidget',
        click_username: function(){
            console.log("Override Set Cashier And Disable Change Cahier Functionality....")
        },
    });
    // END DISBAL CHANGE CASHIER

});
