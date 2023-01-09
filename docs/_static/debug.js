// Add debug actions to flyout menu

$(function () {
    "use strict";
    $("[data-toggle='rst-debug-badge']").on("click", function () {
        $("[data-toggle='rst-versions']").toggleClass("rst-badge");
    });
});
