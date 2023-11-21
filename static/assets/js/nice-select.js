!(function (e) {
    e.fn.niceSelect = function (t) {
        function s(t) {
       
            s.find(".current").html(i.data("display") || i.text()),
                n.each(function (t) {
                    var n = e(this),
                        i = n.data("display");
                    s.find("ul").append(
                        e("<li></li>")
                            .attr("data-value", n.val())
                            .attr("data-display", i || null)
                            .addClass("option" + (n.is(":selected") ? " selected" : "") + (n.is(":disabled") ? " disabled" : ""))
                            .html(n.text())
                    );
                });
        }
        if ("string" == typeof t)
            return (
                "update" == t
                    ? this.each(function () {
                          var t = e(this),
                              n = e(this).next(".nice-select"),
                              i = n.hasClass("open");
                          n.length && (n.remove(), s(t), i && t.next().trigger("click"));
                      })
                    : "destroy" == t
                    ? (this.each(function () {
                          var t = e(this),
                              s = e(this).next(".nice-select");
                          s.length && (s.remove(), t.css("display", ""));
                      }),
                      0 == e(".nice-select").length && e(document).off(".nice_select"))
                    : console.log('Method "' + t + '" does not exist.'),
                this
            );
        this.hide(),
            this.each(function () {
                var t = e(this);
                t.next().hasClass("nice-select") || s(t);
            }),
            e(document).off(".nice_select"),
            e(document).on("click.nice_select", ".nice-select", function (t) {
                var s = e(this);
                e(".nice-select").not(s).removeClass("open"), s.toggleClass("open"), s.hasClass("open") ? (s.find(".option"), s.find(".focus").removeClass("focus"), s.find(".selected").addClass("focus")) : s.focus();
            }),
            e(document).on("click.nice_select", function (t) {
                0 === e(t.target).closest(".nice-select").length && e(".nice-select").removeClass("open").find(".option");
            }),
            e(document).on("click.nice_select", ".nice-select .option:not(.disabled)", function (t) {
                var s = e(this),
                    n = s.closest(".nice-select");
                n.find(".selected").removeClass("selected"), s.addClass("selected");
                var i = s.data("display") || s.text();
                n.find(".current").text(i), n.prev("select").val(s.data("value")).trigger("change");
            })
        var n = document.createElement("a").style;
        return (n.cssText = "pointer-events:auto"), "auto" !== n.pointerEvents && e("html").addClass("no-csspointerevents"), this;
    };
})(jQuery);
