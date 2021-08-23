$(document).ready(function () {
    var url = new URL(document.URL);
    var c = url.searchParams.get("days");
    let days = 1;
    let ah
    if (c) {
        days = c
    }

    let v;
    let h;
    let sd = false, ed = false;


    v = $('.dropdown #1').data("cost")
    h = $('.dropdown #1').data("href")
    ah = $('#ahref').data("href")


    $('.wrapper-home .dropdown .btn').html($('.dropdown #1').html())
    $('.wrapper-home .done').attr("href", h)
    $('#ahref').attr("href", ah)
    $('.wrapper-home .total_cost_e').html($('.dropdown #1').data("cost") + " " + " млн сумов")
    $('.wrapper-room .total_cost_e').html($('.wrapper-room .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
    $('.wrapper-booking .total_cost_e').html($('.wrapper-booking .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")


    let updateHref = () => {
        let _h = h;
        let _ah = ah;

        if (sd) {
            _h += `?sd=${sd}&ed=${ed}&days=${days}`;
            _ah += `?sd=${sd}&ed=${ed}&days=${days}`;
        }
        $('.wrapper-home .done').attr("href", _h)
        $('#ahref').attr("href", _ah)
    };
    var today = new Date()

    $('#picker').daterangepicker({
            isInvalidDate: function (ele) {
                var currDate = moment(ele._d).format('YYYY-M-DD');
                return qwqw.indexOf(currDate) != -1;
            },
            minDate: today,
            autoApply: true,
            linkedCalendars: false,
            opens: 'center',
        }
        , function (start, end) {
            sd = start.format('MM-DD-YYYY');
            ed = end.format('MM-DD-YYYY');
            $(this).val("asdasd")
            days = (end - start + 1) / (1000 * 60 * 60 * 24) - 1;
            $('.total_cost_e').html(v * parseInt(days) + " " + " млн сумов")
            $('.wrapper-room .total_cost_e').html($('.wrapper-room .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
            $('.wrapper-booking .total_cost_e').html($('.wrapper-booking .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
            $('[name = "days"]').val(days)
            $('[name = "start_date"]').val(sd)
            $('[name = "finish_date"]').val(ed)

            updateHref();
        }
    );


    $(' .dropdown .dropdown-item').on('click', function () {
        // alert(v)
        v = $(this).data("cost");
        h = $(this).data("href");

        updateHref();
        $('.wrapper-home .dropdown .btn').html($(this).html())
        $('.total_cost_e').html(parseInt(v) * parseInt(days) + " " + " млн сумов")
        $('.wrapper-room .total_cost_e').html($('.wrapper-room .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")
        $('.wrapper-booking .total_cost_e').html($('.wrapper-booking .total_cost_e').data("cost") * parseInt(days) + " " + " млн сумов")


    })
    // $('[name = "start_date"]').val(sd)
    // $('[name = "finish_date"]').val(ed)

    $('[name = "days"]').val(days)
    // $('#post_p').attr("action", 'asdasdas')
    updateHref();


});
