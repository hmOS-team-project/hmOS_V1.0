const crypto = require('crypto')

module.exports = {
    MD5_SUFFIX: 'FDSW$t34tregt5tO&$#x`$^%^%6YE*&OI$HRLuy87odlfhasdhfhh',
    md5: function(str) {
        var obj = crypto.createHash('md5')
        obj.update(str)
        return obj.digest('hex')
    }
}