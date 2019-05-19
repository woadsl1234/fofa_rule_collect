
function random_select() {
    var color = ['error', 'success','info' ,'warning']
    var value = array[Math.round(Math.random()*(color.length-1))];  //随机抽取一个值
    return value
}

$('#id').attr('class',random_select())