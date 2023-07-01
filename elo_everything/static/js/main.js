$(document).ready(function() {
    $("#vote-button1, #vote-button2").click(function() {
        var conceptId = $(this).data("concept-id");
        $.ajax({
            url: "/vote",
            type: "POST",
            data: { concept_id: conceptId },
            success: function(response) {
                if (response.status === "success") {
                    alert(response.vote_success);
                    location.reload();
                } else {
                    alert(response.vote_error);
                }
            },
            error: function() {
                alert("An error occurred. Please try again.");
            }
        });
    });
});