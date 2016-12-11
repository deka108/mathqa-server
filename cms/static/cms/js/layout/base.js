$( document ).ready(function() {
    // Create title
    $(".title").append(en.cms.title.dashboard);
    $(".title-page").append(en.cms.title.dashboard);

    // Menu
    $("#nav_application").append(en.cms.menu.application);
    $("#sign-out").append(en.cms.menu.sign_out);

    // Management
    $('#manage-topic').append(en.cms.management.topic);
    $('#manage-concept').append(en.cms.management.concept);
    $('#manage-paper').append(en.cms.management.paper);
    $('#manage-question').append(en.cms.management.question);
    $('#manage-user').append(en.cms.management.user);
    $('#manage-quiz').append(en.cms.management.quiz);
    $('#manage-contest').append(en.cms.management.contest);
    $('#manage-formula').append(en.cms.management.formula);

    $('.link-formset').formset({
        addText: 'Add key point',
        deleteText: 'Remove'
    });
});
