$(".btn-quickview").click(function(event) {
    var post_id = $(event.target).data("post-id")
    console.log(event.target, post_id)
    var url = "/post/" + post_id + "/ajax"
    $.get(url, function(data) {
        $("#jobDetailModal").find(".modal-dialog").html(data)
    })
})



$(".btn-quickview").click(function(event) {
    var post_id = $(event.target).data("post-id")
    console.log(event.target, post_id)
    var url = "/post/" + post_id + "/ajax"
    $.get(url, function(data) {
        $("#jobDetail").find(".jobDetail").html(data)
    })
})


$(document).ready(function() {
    $("#load_detail").on("click", function() {
        $("#content").load("content.html");
    });
});