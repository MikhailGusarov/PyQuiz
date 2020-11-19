if(document.getElementsByClassName('show_answer')[0] != undefined) {
    document.getElementsByClassName('show_answer')[0].onclick = function(){
        document.getElementsByClassName('show_answer')[0].style = 'display:none';
        document.getElementsByClassName('back')[0].style = 'display:block';
        document.getElementsByClassName('answer')[0].style = 'display:block';
    }
}