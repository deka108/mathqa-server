$.extend( true, $.fn.dataTable.defaults, {
    "autoWidth": false,
    "columnDefs": [
        { width: '10%', targets: 0 },
        { width: '15%', targets: 1 },
        { width: '10%', targets: 2 },
        { width: '10%', targets: 3 },
        { width: '25%', targets: 4 },
        { width: '10%', targets: 5 },
        { width: '10%', targets: 6 },
    ],
    "order": [[ 0, "asc" ]]
} );

$(document).ready(function() {
    $('#items').DataTable();

    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-user').append(en.cms.breadcrumb.user);

    // Table headers
    $('#header-username').append(en.cms.header.username);
    $('#header-email').append(en.cms.header.email);
    $('#header-firstname').append(en.cms.header.firstname);
    $('#header-lastname').append(en.cms.header.lastname);
    $('#header-lastlogin').append(en.cms.header.lastlogin);
    $('#header-isstaff').append(en.cms.header.isstaff);
    $('#header-isactive').append(en.cms.header.isactive);

    $('#main-title').append(en.cms.breadcrumb.user);

    $('#add').append(en.cms.action.add_user);
} );
