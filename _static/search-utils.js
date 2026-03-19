/**
 * Search utilities for OpenSPP documentation
 * Provides $.getQueryParameters() and $u utilities that searchtools.js expects
 */

// Ensure DOCUMENTATION_OPTIONS.URL_ROOT is set
if (typeof DOCUMENTATION_OPTIONS !== 'undefined' && !DOCUMENTATION_OPTIONS.URL_ROOT) {
    DOCUMENTATION_OPTIONS.URL_ROOT = document.querySelector('html').getAttribute('data-content_root') || './';
}

// Add $.getQueryParameters if it doesn't exist
if (typeof jQuery !== 'undefined' && !jQuery.getQueryParameters) {
    jQuery.getQueryParameters = function(s) {
        if (typeof s === 'undefined')
            s = document.location.search;
        var parts = s.substr(s.indexOf('?') + 1).split('&');
        var result = {};
        for (var i = 0; i < parts.length; i++) {
            var tmp = parts[i].split('=', 2);
            var key = decodeURIComponent(tmp[0]);
            var value = decodeURIComponent(tmp[1]);
            // Store values as arrays to match expected behavior
            if (!result[key]) {
                result[key] = [];
            }
            result[key].push(value);
        }
        return result;
    };
}

// Add $.urlencode if it doesn't exist
if (typeof jQuery !== 'undefined' && !jQuery.urlencode) {
    jQuery.urlencode = encodeURIComponent;
}

// Add $u utility object (replaces underscore.js functionality)
if (typeof $u === 'undefined') {
    var $u = {
        indexOf: function(array, item) {
            return array.indexOf(item);
        },
        contains: function(array, item) {
            return array.indexOf(item) !== -1;
        },
        every: function(array, fn) {
            return array.every(fn);
        },
        each: function(array, fn) {
            array.forEach(fn);
        },
        map: function(array, fn) {
            return array.map(fn);
        },
        max: function(array) {
            return Math.max.apply(null, array);
        }
    };
}

// Add jQuery.fn.highlightText plugin for search term highlighting
if (typeof jQuery !== 'undefined' && !jQuery.fn.highlightText) {
    jQuery.fn.highlightText = function(text, className) {
        function highlight(node) {
            if (node.nodeType === 3) { // TEXT_NODE
                var val = node.nodeValue;
                var pos = val.toLowerCase().indexOf(text.toLowerCase());
                if (pos >= 0 &&
                    !jQuery(node.parentNode).hasClass(className) &&
                    !jQuery(node.parentNode).hasClass('nohighlight')) {
                    var span = document.createElement('span');
                    span.className = className;
                    span.appendChild(document.createTextNode(val.substr(pos, text.length)));

                    var rest = document.createTextNode(val.substr(pos + text.length));
                    node.parentNode.insertBefore(span, node.nextSibling);
                    node.parentNode.insertBefore(rest, span.nextSibling);
                    node.nodeValue = val.substr(0, pos);

                    // Recursively highlight remaining text
                    if (rest.nodeValue.toLowerCase().indexOf(text.toLowerCase()) >= 0) {
                        highlight(rest);
                    }
                }
            } else if (node.nodeType === 1 && node.childNodes &&
                       !/(script|style)/i.test(node.tagName) &&
                       !/(button|select|textarea)/i.test(node.tagName)) {
                Array.from(node.childNodes).forEach(function(child) {
                    highlight(child);
                });
            }
        }

        return this.each(function() {
            highlight(this);
        });
    };
}
