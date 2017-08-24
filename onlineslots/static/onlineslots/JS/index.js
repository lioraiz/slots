$(document).ready(function() {
// Hide the div appearing after user runs out of credit
$(".reset").click(function() {
    $(".endgame").css("display", "none");
})

$(".play").click(function() {
    var suits = ["club", "diamond", "heart", "spade"];
    var result = "";
    // Spin the reels
    if ($("reel").attr("class") != "spin"){
        $("reel").toggleClass("spin").removeClass("club diamond heart spade");
        $(".cashout").removeClass("win");
    }
    else {
    // Stop the reels
        $("reel").toggleClass("spin");
        $("reel").each(function() {
            $(this).toggleClass(suits[Math.floor(Math.random() * suits.length)]);
        });
        // Round outcome
        if (($("#reel1").attr("class")) == ($("#reel2").attr("class")) && ($("#reel1").attr("class")) == ($("#reel3").attr("class"))){
            $(".cashout").addClass("win");
            var result = "win"
        } else {
            var result = "lose"
        }
        // Update credit using ajax
        $.ajax({
                type:"POST",
                url:"/gameresult/",
                data: {
                    "result": result
                },
                success:function(data){
                details = JSON.parse(data)
                    console.log(details)
                    console.log(details.restart)

                    $('.funds').text(details.userfund)
                    $('.endgame').hide()
                    // Out of credit
                    if (!details.restart == "") {
                        $('.endgame').show()
                    }
                }
       })
    }                              
});
});