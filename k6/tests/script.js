import http from 'k6/http';
import { check, sleep } from 'k6';
import { getOptions } from '../scenarios/scenarios.js';

export const options = getOptions(__ENV.SCENARIO);

export default function script() {
    console.log("Executando o script importado!");

    const url = __ENV.API_URL;

    console.log("-------------->>>>" + url);

    const res = http.get(url);
    check(res, { 'status foi 200': (r) => r.status == 200 });

    sleep(1);
}
