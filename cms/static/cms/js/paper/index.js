$.extend( true, $.fn.dataTable.defaults, {
    "autoWidth": false,
    "columnDefs": [
        { width: '5%', targets: 0 },
        { width: '20%', targets: 1 },
        { width: '40%', targets: 2 },
        { width: '15%', targets: 3 },
        { width: '20%', targets: 4 },
    ],
    "order": [[ 0, "asc" ]]
} );

$(document).ready(function() {
    $('#items').DataTable();

    // Breadcum
    $('#breadcrumb-home').append(en.cms.breadcrumb.home);
    $('#breadcrumb-paper').append(en.cms.breadcrumb.paper);

    // Table headers
    $('#header-year').append(en.cms.header.year);
    $('#header-month').append(en.cms.header.month);
    $('#header-number').append(en.cms.header.number);
    $('#header-no').append(en.cms.header.no);

    $('#main-title').append(en.cms.breadcrumb.paper);

    $('#add').append(en.cms.action.add_paper);
} );
