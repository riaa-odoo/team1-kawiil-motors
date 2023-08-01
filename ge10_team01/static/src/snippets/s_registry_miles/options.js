odoo.define('ge10_team01.s_registry_miles_options', function (require) {
    'use strict';

    const options = require('web_editor.snippets.options');

    options.registry.RegistryMiles = options.Class.extend({

        //--------------------------------------------------------------------------
        // Options
        //--------------------------------------------------------------------------

        /**
        * Changes the total mileage widget style.
        *
        * @see this.selectClass for parameters
        */
        layout: function (previewMode, widgetValue, params) {
            this.$target[0].dataset.layout = widgetValue;
        },

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * @override
         */
        _computeWidgetState: function (methodName, params) {
            if (methodName === 'layout') {
                return this.$target[0].dataset[methodName];
            }
            return this._super(...arguments);
        },
    });
});
