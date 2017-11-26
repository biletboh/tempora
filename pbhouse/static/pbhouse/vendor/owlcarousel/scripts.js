
$(document).ready(function() {
    $("#projects").addClass("js-reveal");
    var j = true;
    var i = "#owl-main";
    function a() {
        if (!j) {
            $(i + " .caption .fadeIn-1, " + i + " .caption .fadeIn-2, " + i + " .caption .fadeIn-3").stop().delay(800).animate({
                opacity: 0
            }, {
                duration: 400,
                easing: "easeInCubic"
            })
        } else {
            $(i + " .caption .fadeIn-1, " + i + " .caption .fadeIn-2, " + i + " .caption .fadeIn-3").css({
                opacity: 0
            })
        }
    }

    function c() {
        if (!j) {
            $(i + " .caption .fadeInDown-1, " + i + " .caption .fadeInDown-2, " + i + " .caption .fadeInDown-3").stop().delay(800).animate({
                opacity: 0,
                top: "-15px"
            }, {
                duration: 400,
                easing: "easeInCubic"
            })
        } else {
            $(i + " .caption .fadeInDown-1, " + i + " .caption .fadeInDown-2, " + i + " .caption .fadeInDown-3").css({
                opacity: 0,
                top: "-15px"
            })
        }
    }

    function l() {
        if (!j) {
            $(i + " .caption .fadeInUp-1, " + i + " .caption .fadeInUp-2, " + i + " .caption .fadeInUp-3").stop().delay(800).animate({
                opacity: 0,
                top: "15px"
            }, {
                duration: 400,
                easing: "easeInCubic"
            })
        } else {
            $(i + " .caption .fadeInUp-1, " + i + " .caption .fadeInUp-2, " + i + " .caption .fadeInUp-3").css({
                opacity: 0,
                top: "15px"
            })
        }
    }

    function b() {
        if (!j) {
            $(i + " .caption .fadeInLeft-1, " + i + " .caption .fadeInLeft-2, " + i + " .caption .fadeInLeft-3").stop().delay(800).animate({
                opacity: 0,
                left: "15px"
            }, {
                duration: 400,
                easing: "easeInCubic"
            })
        } else {
            $(i + " .caption .fadeInLeft-1, " + i + " .caption .fadeInLeft-2, " + i + " .caption .fadeInLeft-3").css({
                opacity: 0,
                left: "15px"
            })
        }
    }

    function e() {
        if (!j) {
            $(i + " .caption .fadeInRight-1, " + i + " .caption .fadeInRight-2, " + i + " .caption .fadeInRight-3").stop().delay(800).animate({
                opacity: 0,
                left: "-15px"
            }, {
                duration: 400,
                easing: "easeInCubic"
            })
        } else {
            $(i + " .caption .fadeInRight-1, " + i + " .caption .fadeInRight-2, " + i + " .caption .fadeInRight-3").css({
                opacity: 0,
                left: "-15px"
            })
        }
    }

    function f() {
        $(i + " .active .caption .fadeIn-1").stop().delay(500).animate({
            opacity: 1
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeIn-2").stop().delay(700).animate({
            opacity: 1
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeIn-3").stop().delay(1000).animate({
            opacity: 1
        }, {
            duration: 800,
            easing: "easeOutCubic"
        })
    }

    function g() {
        $(i + " .active .caption .fadeInDown-1").stop().delay(500).animate({
            opacity: 1,
            top: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInDown-2").stop().delay(700).animate({
            opacity: 1,
            top: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInDown-3").stop().delay(1000).animate({
            opacity: 1,
            top: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        })
    }

    function h() {
        $(i + " .active .caption .fadeInUp-1").stop().delay(500).animate({
            opacity: 1,
            top: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInUp-2").stop().delay(700).animate({
            opacity: 1,
            top: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInUp-3").stop().delay(1000).animate({
            opacity: 1,
            top: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        })
    }

    function k() {
        $(i + " .active .caption .fadeInLeft-1").stop().delay(500).animate({
            opacity: 1,
            left: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInLeft-2").stop().delay(700).animate({
            opacity: 1,
            left: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInLeft-3").stop().delay(1000).animate({
            opacity: 1,
            left: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        })
    }

    function d() {
        $(i + " .active .caption .fadeInRight-1").stop().delay(500).animate({
            opacity: 1,
            left: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInRight-2").stop().delay(700).animate({
            opacity: 1,
            left: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        });
        $(i + " .active .caption .fadeInRight-3").stop().delay(1000).animate({
            opacity: 1,
            left: "0"
        }, {
            duration: 800,
            easing: "easeOutCubic"
        })
    }
    $(i).owlCarousel({
        autoPlay: 5000,
        stopOnHover: true,
        navigation: true,
        pagination: true,
        singleItem: true,
        addClassActive: true,
        transitionStyle: "fade",
        navigationText: ["<i class='fa fa-angle-left' aria-hidden='true'></i>", "<i class='fa fa-angle-right' aria-hidden='true'></i>"],
        afterInit: function() {
            f();
            g();
            h();
            k();
            d()
        },
        afterMove: function() {
            f();
            g();
            h();
            k();
            d()
        },
        afterUpdate: function() {
            f();
            g();
            h();
            k();
            d()
        },
        startDragging: function() {
            j = true
        },
        afterAction: function() {
            a();
            c();
            l();
            b();
            e();
            j = false
        }
    });
    /*
    $(".slider-next").click(function() {
        owl.trigger("owl.next")
    });
    $(".slider-prev").click(function() {
        owl.trigger("owl.prev")
    })
    */
});