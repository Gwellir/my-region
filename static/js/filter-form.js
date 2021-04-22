//const filterParams = ['district', 'region', 'type', 'level']

function restrictRegions(district_id) {
    for (option of $("a.region-option")) {
        if (district_id && option.dataset.district && +option.dataset.district !== district_id)
            option.hidden = true;
        else
            option.hidden = false;
    }
}

function setDropdownValue() {
    let btn = $(this).parents(".btn-group").find('.btn');
    let value = $(this).data('value')
    btn.html($(this).text());
    btn.val(value);
    if (btn.data('name') === 'district')
        restrictRegions(value);
}

$(document).ready(function() {
    let urlParams = new URLSearchParams(window.location.search);
    let filterBtns = [...$(document).find('.filter-form button.dropdown-toggle')];
    let filterParams = filterBtns.map(function(btn) {
        return btn.dataset.name;
    });
    for (param of filterParams) {
        value = urlParams.get(param);
        if (value) {
            let option = $(document).find(`.${param}-option[data-value="${value}"]`)
            setDropdownValue.call(option);
        }
    }
});

$(".dropdown-menu a.dropdown-item").click(setDropdownValue);

$("#filter-submit").click(function(e) {
    e.preventDefault();
    let url = new URL(window.location.origin + "/travel/");
    for (el of $(".filter-form button.dropdown-toggle")) {
        if (el.value)
            url.searchParams.append(el.dataset.name, el.value);
    }
    for (el of $(".filter-form .dropdown-item input")) {
        if (el.value)
            url.searchParams.append(el.dataset.name, el.value);
    }
    document.location = url;
});