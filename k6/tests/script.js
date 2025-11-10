import http from 'k6/http';
import { check, sleep } from 'k6';

export default function script() {
    console.log("Executando o script importado!");

    const url = __ENV.API_URL;

    console.log("-------------->>>>" + url);

    const res = http.get('https://quickpizza.grafana.com');
    check(res, { 'status foi 200': (r) => r.status == 200 });

    sleep(1);
}
