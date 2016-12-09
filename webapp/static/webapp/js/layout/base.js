var MQ = MathQuill.getInterface(2);

$( document ).ready(function() {
    // Create title
    $(".title").append(en.title.dashboard);

    // Menu
    $("#menu-home").append(en.menu.home);
    $("#menu-topic").append(en.menu.topic);
    $("#menu-quiz").append(en.menu.quiz);
    $("#menu-contest").append(en.menu.contest);
    $("#menu-leaderboard").append(en.menu.leaderboard);
    $("#menu-proficiency").append(en.menu.proficiency);

    $("#sign-out").append(en.menu.sign_out);
    $("#register").append(en.menu.register);
    $("#login").append(en.menu.login);

    $("#search-box").attr("onkeyup", "Preview.Update()");
    $("#btn-search").click(function() {
        window.location.href = "/search_question?keyword=" + document.getElementById("search-box").value;
    });

    $("#btn-1").click(function(){
        $("#search-box").val($("#search-box").val() + "\\frac{x}{y}");
        Preview.Update();
    });
    $("#btn-2").click(function(){
        $("#search-box").val($("#search-box").val() + "e^x");
        Preview.Update();
    });
    $("#btn-3").click(function(){
        $("#search-box").val($("#search-box").val() + "x^2");
        Preview.Update();
    });
    $("#btn-4").click(function(){
        $("#search-box").val($("#search-box").val() + "{x}_{2}");
        Preview.Update();
    });
    $("#btn-5").click(function(){
        $("#search-box").val($("#search-box").val() + "\\sqrt{x}");
        Preview.Update();
    });
    $("#btn-6").click(function(){
        $("#search-box").val($("#search-box").val() + "\\sqrt[3]{x}");
        Preview.Update();
    });
    $("#btn-7").click(function(){
        $("#search-box").val($("#search-box").val() + "\\int_{-1}^{1} xdx");
        Preview.Update();
    });
    $("#btn-8").click(function(){
        $("#search-box").val($("#search-box").val() + "\\sum_{i=0}^{n} {a}_{n}");
        Preview.Update();
    });
    $("#btn-9").click(function(){
        $("#search-box").val($("#search-box").val() + "\\overrightarrow{AB}");
        Preview.Update();
    });
    $("#btn-10").click(function(){
        $("#search-box").val($("#search-box").val() + "\\sin x");
        Preview.Update();
    });
    $("#btn-11").click(function(){
        $("#search-box").val($("#search-box").val() + "\\cos x");
        Preview.Update();
    });
    $("#btn-12").click(function(){
        $("#search-box").val($("#search-box").val() + "\\tan x");
        Preview.Update();
    });
    $("#btn-13").click(function(){
        $("#search-box").val($("#search-box").val() + "\\cot x");
        Preview.Update();
    });
    $("#btn-14").click(function(){
        $("#search-box").val($("#search-box").val() + "\\lim_(n \to \infty)");
        Preview.Update();
    });
    $("#btn-15").click(function(){
        $("#search-box").val($("#search-box").val() + "\\log x");
        Preview.Update();
    });
    $("#btn-16").click(function(){
        $("#search-box").val($("#search-box").val() + "\\ln x");
        Preview.Update();
    });
});
