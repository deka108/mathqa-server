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
});
