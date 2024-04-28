# https://leetcode.com/problems/repeat-string/description/

declare global {
    interface String {
        replicate(times: number): string;
    }
}

String.prototype.replicate = function(times): string {

    var replt = "";
    for (var i = 0; i < times; i++) {
        replt += this
    }

    return replt;
    
}
