
import * as fs from 'fs'

// carrega as variáveis entre os scripts
export function GetData(){
    let rawdata = fs.readFileSync('envData.json');
    let data = JSON.parse(rawdata);
    return {data};
}