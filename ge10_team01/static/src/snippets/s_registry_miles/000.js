odoo.define('ge10_team01.s_registry_miles', function (require) {
    'use strict';

    const { ColorpickerWidget } = require('web.Colorpicker');
    const publicWidget = require('web.public.widget');
    const weUtils = require('web_editor.utils');

    const RegistryMilesWidget = publicWidget.Widget.extend({
        selector: '.s_registry_miles',
        disabledInEditableMode: false,

        /**
         * @override
         */
        start() {
            this.$wrapper = this.$('.s_registry_miles_wrapper');
            this.borderColor = this._ensureCssColor(this.el.dataset.borderColor);
            this.layout = this.el.dataset.layout;
            this.textColor = this._ensureCssColor(this.el.dataset.textColor);

            this._render();
            return this._super(...arguments);
        },

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Ensures the color is an actual css color. In case of a color variable,
         * the color will be mapped to hexa.
         *
         * @private
         * @param {string} color
         * @returns {string}
         */
        _ensureCssColor: function (color) {
            if (ColorpickerWidget.isCSSColor(color)) {
                return color;
            }
            return weUtils.getCSSVariableValue(color) || this.defaultColor;
        },
        /**
         * Draws the total mileage with the user selected layout.
         *
         * @private
         */
        _render: async function () {
            var vals = await this._rpc({
                route: '/motorcycle_registry/get_mileage'
            });

            this.$wrapper.empty();

            if (this.layout === 'box') {
                this._drawBox(vals);
            } else if (this.layout === 'text') {
                this._drawText(vals);
            }
        },

        //--------------------------------------------------------------------------
        // Canvas drawing methods
        //--------------------------------------------------------------------------

        /**
         * Draws the box layout for the total mileage count.
         *
         * @private
         */
        _drawBox: function (vals) {
            let list = $('<ul class="list-group list-group-horizontal justify-content-center"/>').appendTo(this.$wrapper)[0];

            [...vals.total_mileage.toString()].forEach(number => {
                let listItem = $(`<li class='col list-group-item text-center py-2'><h4>${number}</h4></li>`);
                listItem[0].style.backgroundColor = 'rgb(0,0,0,0)';
                listItem[0].style.borderColor = this.borderColor;
                listItem[0].style.color = this.textColor;
                listItem.appendTo(list);
            });
        },
        /**
         * Draws the text layout for the total mileage count.
         *
         * @private
         */
        _drawText: function (vals) {
            let textWrapper = $('<h3/>').attr({
                class: 's_registry_miles_text_wrapper o_default_snippet_text',
            });
            textWrapper[0].style.color = this.textColor;
            textWrapper.text(vals.total_mileage.toLocaleString());
            textWrapper.appendTo(this.$wrapper);
        },
    });

    publicWidget.registry.RegistryMiles = RegistryMilesWidget;

    return RegistryMilesWidget;
});
