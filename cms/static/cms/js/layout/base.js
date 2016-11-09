$( document ).ready(function() {
    // Create title
    $(".title").append(en.cms.title.dashboard);
    $(".title-page").append(en.cms.title.dashboard);

    // Menu
    $("#nav_applicaiton").append(en.cms.menu.application);
    $("#sign-out").append(en.cms.menu.sign_out);

    // Management
    $('#manage-topic').append(en.cms.management.topic);
    $('#manage-concept').append(en.cms.management.concept);
    $('#manage-question').append(en.cms.management.question);
    $('#manage-tag').append(en.cms.management.tag);
    $('#manage-quiz').append(en.cms.management.quiz);
    $('#manage-contest').append(en.cms.management.contest);
});
