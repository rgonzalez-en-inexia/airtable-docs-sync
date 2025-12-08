# 🗂️ Airtable Database Structure - Aulas

> **Last update**: 2025-12-08 22:04:10
> **Base**: aulas (Aulas)
> **Auto-generated** - Do not edit manually

## 📊 Summary

- **Tables**: 44
- **Total fields**: 1554
- **Base ID**: `appEuz3PoChgzMmCH`

- **singleSelect fields**: 119
- **multipleSelects fields**: 1
- **number fields**: 278
- **date fields**: 8
- **formula fields**: 191

---

## 📋 1. ActividadesPorEstudiante

*Table ID: `tbl8ySdsaC21EJ4NF`*
*Fields: 4*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTestudiante**<br>`fldoCLSypuYoGCiTE` | `singleLineText` | Type: singleLineText |  |
| **OA**<br>`fld9yfu0FvMAnrd98` | `singleLineText` | Type: singleLineText |  |
| **ActividadObjetivo**<br>`fldLxIGNbm0YMlu8G` | `singleLineText` | Type: singleLineText |  |
| **ActividadMotivacion**<br>`fldS3vcVp7qaMsw35` | `singleLineText` | Type: singleLineText |  |

---

## 📋 2. Apoderados

*Table ID: `tble33sHcPT2atT4t`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTapoderado**<br>`fldcn0D0OCvIgDAGP` | `singleLineText` | Type: singleLineText |  |
| **ApodVinculo**<br>`fldHVIXNXhaILeKTf` | `singleLineText` | Type: singleLineText |  |
| **ApodPaterno**<br>`fldklMIFtsbEFL35Y` | `singleLineText` | Type: singleLineText |  |
| **ApodMaterno**<br>`fldel3vWYkKVe0AIb` | `singleLineText` | Type: singleLineText |  |
| **ApodNombres**<br>`fld97VQIB672HXt4Q` | `singleLineText` | Type: singleLineText |  |
| **ApodNombreCompleto**<br>`fldLuywCGWOuMkE2a` | `formula` | Calculated field | Formula: `{fld97VQIB672HXt4Q} & " " & {fldklMIFtsbEFL35Y} & ...` |
| **ApodEmail**<br>`fldHoJMdU3zWjUzLN` | `email` | Email address |  |
| **ApodCuadrante**<br>`fldbdH2nPaxWCnSmK` | `number` | Numeric field |  |
| **ApodEstudAnnoIngreso**<br>`fldbEc9yIO6QGLDJk` | `number` | Numeric field |  |
| **Estudiantes**<br>`fldEZhPzsDy75fGXj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 3. BancoActividades

*Table ID: `tblwsXutO3x5qH72O`*
*Fields: 83*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ActividadSerial**<br>`fldxNnPCbJY8mYIsN` | `autoNumber` | Type: autoNumber |  |
| **ActLinkImagen**<br>`fldurOkhrjhDz0Qtw` | `url` | URL link |  |
| **OA**<br>`flddTokmElFBp6pkc` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **OAdescripcion**<br>`fldw71tCIi5qj22e2` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAeje**<br>`fld4iDWomp0OcuwXj` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ActRUT**<br>`fldCOk3DxRyCQVWpZ` | `singleLineText` | Type: singleLineText |  |
| **ActLogrado**<br>`fldg3XtX5IAB8om86` | `number` | Numeric field |  |
| **ActFechaLogrado**<br>`fldaJRy2mDN48rgt0` | `singleLineText` | Type: singleLineText |  |
| **ActConSinEscritura**<br>`fldBoUre58CGca581` | `singleLineText` | Type: singleLineText |  |
| **ActTextoDelEstudiante**<br>`fldvQWbNvYWHqMc0N` | `richText` | Rich text with formatting |  |
| **ActValidaAutomatica**<br>`fldtXHtyaLsYj3cl0` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldzfKcwcFo5GG6PR}>5, {fldCOk3Dx...` |
| **PromptIA**<br>`fldUCbQdYaF6h2djL` | `number` | Numeric field |  |
| **IAexecTimeSec**<br>`fldbaFQSCXkl7TEYc` | `number` | Numeric field |  |
| **AlarmaExecIA**<br>`fldRfI6zIzBVh8v4y` | `formula` | Calculated field | Formula: `IF(
  {fldbaFQSCXkl7TEYc} > 40, 911, 0
)
` |
| **FlagCrearImagen**<br>`fld8Mwo007cRt8RJM` | `formula` | Calculated field | Formula: `IF(AND(LEFT({flddTokmElFBp6pkc},2)="HI",{fldu7PUgd...` |
| **ActScriptHtml**<br>`fldXMR0owlyDX7aRA` | `multilineText` | Multi-line text |  |
| **ActRespuestasCorrectas**<br>`fldPyNe3VZ3JrY1fB` | `number` | Numeric field |  |
| **ActCantidadPreguntas**<br>`fldPUR2cufkg9zESp` | `number` | Numeric field |  |
| **FechaScriptHtml**<br>`fldobqJVHtkDUdFtH` | `singleLineText` | Type: singleLineText |  |
| **ActLinkVideo**<br>`fldQJvuRdb72dwm1y` | `url` | URL link |  |
| **VersionCreaScriptHtml**<br>`fld3bptE98a6dEHpa` | `singleLineText` | Type: singleLineText |  |
| **ActNombre**<br>`fldKj3mJChhvMwS4e` | `singleLineText` | Type: singleLineText |  |
| **ActMotivacion**<br>`fldozydnaDw6e1djZ` | `multilineText` | Multi-line text |  |
| **OAAntiguedad**<br>`fldOjtyiQM9Dmnb3n` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAmateria**<br>`fld2QsxKPhd4whemC` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ActActividadEstudiante**<br>`fldORdf3LHFpjo7GH` | `multilineText` | Multi-line text |  |
| **ActTexto**<br>`fldNNeiHCe1CMfUtB` | `multilineText` | Multi-line text |  |
| **ActMateriales**<br>`fldu7PUgd5HjbLf1F` | `singleLineText` | Type: singleLineText |  |
| **ActTiempoEsperadoMin**<br>`fldzfKcwcFo5GG6PR` | `number` | Numeric field |  |
| **ActEnunciadoEvaluacion1**<br>`fld694hDzsabREHSF` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion1**<br>`fldQ7UhqiNxHQaXoa` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta1**<br>`fldNdHOMDBpuN7BsA` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion2**<br>`fld1OizZ41Dz4TBgL` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion2**<br>`fld4hV1Zgx4uwNAYj` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta2**<br>`fldMByzwYudJ5Fy2H` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion3**<br>`fldCmDyd2K1tujr2k` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion3**<br>`fldFdWJPPVDaTu35D` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta3**<br>`fldl3l7qnwZclxUXm` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion4**<br>`fld3rvhLqp7jxGFNT` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion4**<br>`fldsdpZbEP2bnXlWu` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta4**<br>`fldkO7qORvRMX6FB7` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion5**<br>`fldZGDtP5LLpLoM94` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion5**<br>`fldQzSFUQx9itCnlL` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta5**<br>`fldXMKDQkOYzE24m5` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion6**<br>`fldaAQp3kqb59IoQR` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion6**<br>`fldivxfqUieYWWx2v` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta6**<br>`flduOXayfkIiTejBm` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion7**<br>`fldY5Y6V59ZBIGF4U` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion7**<br>`fldum6QOKtxJVwS5r` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta7**<br>`fldpoQ9CvyjdEZZ9T` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion8**<br>`fldXtvf4sAEe75jrP` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion8**<br>`fldNjz7zpv9y26gUF` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta8**<br>`fldqw02Itr4SUi2UJ` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion9**<br>`fldchs1l9V8EQ8gpn` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion9**<br>`fldZe3Wd7QSRE0psE` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta9**<br>`fldVrS41AHel8bVJx` | `singleLineText` | Type: singleLineText |  |
| **ActEnunciadoEvaluacion10**<br>`fldt51uX4h5OAsYup` | `singleLineText` | Type: singleLineText |  |
| **ActAlternativasEvaluacion10**<br>`fldvhyhjq5QgYxu5F` | `singleLineText` | Type: singleLineText |  |
| **ActRespCorrecta10**<br>`fldYgtBlKR8iYPe7t` | `singleLineText` | Type: singleLineText |  |
| **ActLinkRaw**<br>`fldf6OekXAUrXDMVu` | `url` | URL link |  |
| **ActImagenRespuesta**<br>`fldyUOaBtLWaIABuc` | `multipleAttachments` | Type: multipleAttachments |  |
| **ActIndivGrupal**<br>`fldNB8zixESaiJZ0l` | `singleLineText` | Type: singleLineText |  |
| **ActTipoInteligencia**<br>`fld1SfETOZeLkyNi8` | `singleLineText` | Type: singleLineText |  |
| **ActTipoMotivacion**<br>`fld1ru8TBeDUBQ3oc` | `singleLineText` | Type: singleLineText |  |
| **ActAficion1**<br>`fldakgkG4rIAguxBN` | `singleLineText` | Type: singleLineText |  |
| **ActAficion2**<br>`fldZXMJhZdDkxQqBm` | `singleLineText` | Type: singleLineText |  |
| **ActIdolo1**<br>`fldSMgDo5eudVnev0` | `singleLineText` | Type: singleLineText |  |
| **ActIdolo2**<br>`fldSEpSHQ4C1EvWi8` | `singleLineText` | Type: singleLineText |  |
| **ActInstrumento**<br>`fldigdZBCujoDkaRR` | `singleLineText` | Type: singleLineText |  |
| **ActEstiloMusical1**<br>`fld3YcXkKeJonEJRp` | `singleLineText` | Type: singleLineText |  |
| **ActEstiloMusical2**<br>`fldmNt417XY1qzoB0` | `singleLineText` | Type: singleLineText |  |
| **ActAtraccionCelular1**<br>`fldw9aaPV3nlf4CHe` | `singleLineText` | Type: singleLineText |  |
| **ActAtraccionCelular2**<br>`fld7kMhZMR4j9nraD` | `singleLineText` | Type: singleLineText |  |
| **ActNEE**<br>`fldMRTZ4Tcq85reqz` | `singleLineText` | Type: singleLineText |  |
| **ActValoracionEstudiantes**<br>`fldfU0ZLt4TXQNzyE` | `number` | Numeric field |  |
| **ActValoracionDocentes**<br>`fldwG5uyLhhdPWwBd` | `number` | Numeric field |  |
| **ActFechaCreacion**<br>`fldVcCg3e8SmVPVGb` | `createdTime` | Auto-generated creation time |  |
| **ActActiva**<br>`fldN9Xl53kuPGBVPv` | `checkbox` | True/False checkbox |  |
| **TipoPreguntaJF**<br>`fldADSx8szqhbpoFc` | `singleLineText` | Type: singleLineText |  |
| **Origen**<br>`fldELozGD9BSsoDzS` | `singleLineText` | Type: singleLineText |  |
| **VersionProceso**<br>`fldTsOs7bI2YUM6sm` | `singleLineText` | Type: singleLineText |  |
| **Modelo**<br>`fldUhUD22qU3OGXx2` | `singleLineText` | Type: singleLineText |  |
| **TareasEstudiante**<br>`fldMmRSLEFHb2aIkX` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 4. BancoDesafios

*Table ID: `tblwg5UINgGxAQ1Mi`*
*Fields: 6*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Name**<br>`fldgeXJ0zjwC0Jjvi` | `singleLineText` | Type: singleLineText |  |
| **Notes**<br>`fldCuTjI1OIvXn3Ex` | `multilineText` | Multi-line text |  |
| **Assignee**<br>`fldBWxnF1lLa3AtcX` | `singleCollaborator` | Type: singleCollaborator |  |
| **Status**<br>`fldiqDQyBtJcf6mls` | `singleSelect` | Single choice dropdown | `Todo`, `In progress`, `Done` |
| **Attachments**<br>`fldtzhRq020CTR3VL` | `multipleAttachments` | Type: multipleAttachments |  |
| **Attachment Summary**<br>`fldKpuE4BLqBk84VD` | `aiText` | Type: aiText |  |

---

## 📋 5. BrechasPorEstudiante

*Table ID: `tbloGfNpLd8rqhwtc`*
*Fields: 59*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTestudiante**<br>`fldhRID6BoDzE3IiC` | `singleLineText` | Type: singleLineText |  |
| **FechaDiagnostico**<br>`fldiW4QnO8fuzQZBa` | `createdTime` | Auto-generated creation time |  |
| **Fecha2200**<br>`fldUYcZ2bAnRi1hc7` | `createdTime` | Auto-generated creation time |  |
| **Colegio**<br>`fldSu35HpV3bC1Zu3` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Sexo**<br>`flddM4I1dNpYdJfBG` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ColegioSelect**<br>`fldis6ONsafIuseSA` | `singleSelect` | Single choice dropdown | `San Pedro` |
| **OA**<br>`fldLjidEpdQbUmoUb` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **OA2**<br>`fldjfUiBpSnR7Ngjj` | `singleLineText` | Type: singleLineText |  |
| **Materia**<br>`fld63eDbW7zw8zDq5` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Eje**<br>`fldezi2yYVTE6nrxo` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Prompt3000**<br>`fldWmSJRbRZ7o0eLl` | `number` | Numeric field |  |
| **Fecha3000**<br>`fldrgVWKXGnL4Owfr` | `singleLineText` | Type: singleLineText |  |
| **Materia-Eje**<br>`fldAWEUWTsIkyehAx` | `formula` | Calculated field | Formula: `{fld63eDbW7zw8zDq5}&"-"&{fldezi2yYVTE6nrxo}` |
| **OAnivel**<br>`fldQIQWqZf9e7ZOaP` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAnivelTxt**<br>`fldbLXrhPKWCEN6f3` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAdescripcion**<br>`fldE0UAVb9RR61qKV` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAdescripcionResumen**<br>`fldtNv6oyUvzMIcqI` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OA-OAdescripcion**<br>`fldZZknLo5WSfEIZT` | `formula` | Calculated field | Formula: `{fldLjidEpdQbUmoUb}&"-"&{fldE0UAVb9RR61qKV}` |
| **RUTlookUpEstudiantes**<br>`fldcNNqyhrkLOeNFx` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **estudianteNombre**<br>`fldTICUBMYWG0zKuT` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudiantePaterno**<br>`fldFNzuxaMcdX3YTB` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteMaterno**<br>`fldTd0pdWLCLzTOwq` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteNombreCompleto**<br>`fldrwQs9nX21YsDdo` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudiantePerfilPersonal**<br>`fldPgjEqyfmItUMLZ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TipoInteligencia1**<br>`fld5DTaAHgrQkSOm6` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TipoMotivacion**<br>`fldVT2e8gGQTr8kln` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Aficion1**<br>`fld7dbVIjBRwzJrj3` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Aficion2**<br>`fld8vkpqxCkZrLhCM` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Idolo1**<br>`fldA8THQCYxFX6cRx` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Idolo2**<br>`fldAMeiFcadqAdJf8` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Instrumento**<br>`fldMGg2G3yjxcWPnZ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **EstiloMusical1**<br>`fldKONYeVvqw7cipn` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **AtraccionCelular1**<br>`fldAyYrHSapO6bQEq` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **AtraccionCelular2**<br>`fld8YR9eYOnXPa2SJ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Alfabetico**<br>`fldfh58IhD8QrEQho` | `formula` | Calculated field | Formula: `{fldFNzuxaMcdX3YTB}&" "&{fldTd0pdWLCLzTOwq}&", "&{...` |
| **AlfabeticoSelect**<br>`fldDc00DWj6lHa5IG` | `singleSelect` | Single choice dropdown | `Gallegos Salinas, Alan`, `Mejía Castro, Leonardo`, `Vargas Cordero, Clara`, `González Rodríguez, Ana`, `Noir Guzmán, Débora` *(+71 more)* |
| **estudianteNivelActual**<br>`fldwZwzNSOgsbB7s1` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteCursoActual**<br>`fldmpN4UHaMdzvLR7` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **CursoActual**<br>`fldKBNFA2VjZ2mXj5` | `singleSelect` | Single choice dropdown | `1M-A`, `1M-B`, `1M-C`, `1M-D`, `2M-A` *(+13 more)* |
| **Curso-alfabetico**<br>`fldzs2G1sblFNj3F1` | `formula` | Calculated field | Formula: `{fldmpN4UHaMdzvLR7}&" "&{fldfh58IhD8QrEQho}` |
| **FechaProgramada**<br>`fldmCkOoBmIbGis3P` | `dateTime` | Date and time |  |
| **FechaEjecucion**<br>`fldW678FInXedeLtO` | `dateTime` | Date and time |  |
| **Logrado**<br>`fldYmCKeDOUQIvN9x` | `number` | Numeric field |  |
| **FechaLogro**<br>`fldLcIOvlFSL8fLwW` | `dateTime` | Date and time |  |
| **MesLogro**<br>`fldFkAmuO68HY0bTd` | `formula` | Calculated field | Formula: `IF(ISERROR(MONTH({fldLcIOvlFSL8fLwW})),"",MONTH({f...` |
| **MesLogro_txt**<br>`fldMZP0qgR3z6J0S4` | `formula` | Calculated field | Formula: `SWITCH(MONTH({fldLcIOvlFSL8fLwW}),1,'01-Enero',2,'...` |
| **AnnoLogro**<br>`fldl0lAMUxHwKYtxe` | `formula` | Calculated field | Formula: `IF(ISERROR(YEAR({fldLcIOvlFSL8fLwW})),"",YEAR({fld...` |
| **MesDiagnostico**<br>`fldMYTTgx1RHVolEi` | `formula` | Calculated field | Formula: `SWITCH(MONTH({fldiW4QnO8fuzQZBa}),1,'01-Enero',2,'...` |
| **miniExtensions**<br>`fldKkFsyCZfT8RmGv` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Anno5B**<br>`fldVnPXWquK8ebVz9` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Anno6B**<br>`fldqfDRFbeKgI8sFi` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Anno7B**<br>`fld9qE9ZEFkkYpgV1` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Anno8B**<br>`fldYzmXCf4eitWFpf` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Estudiantes copy**<br>`fldlxmCL4mUIxS9VU` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes**<br>`fldoVNuCRqNT7v3iz` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **5B-brechas-LE**<br>`fld4FG2wUmqkuz8WL` | `formula` | Calculated field | Formula: `COUNTALL(IF(AND({fldYmCKeDOUQIvN9x}=911,{fldQIQWqZ...` |
| **Estudiantes copy 2**<br>`fldhJiS5kD0R9cxge` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes copy**<br>`fldeNoMnF9fywlpaB` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes copy**<br>`fldqVoQrf8IGPCFND` | `singleLineText` | Type: singleLineText |  |

---

## 📋 6. CalendarioClases

*Table ID: `tblmEXVSnolxvuYsq`*
*Fields: 3*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Fecha**<br>`fldZZyhk0dGlsVdYW` | `dateTime` | Date and time |  |
| **CalCurso**<br>`fld1nMahMngKJctIT` | `singleLineText` | Type: singleLineText |  |
| **CalMateria**<br>`fldQwwhrqYbJnbj1C` | `singleLineText` | Type: singleLineText |  |

---

## 📋 7. Colegios

*Table ID: `tblhdv30cXgHBSCzg`*
*Fields: 61*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **colegioSigla**<br>`fldhNg1UpLQVTYXLo` | `singleLineText` | Type: singleLineText |  |
| **version020**<br>`fldqk9NpdpWBk0er8` | `singleLineText` | Type: singleLineText |  |
| **FechaCreacion**<br>`fldITZPsZFIYivOct` | `createdTime` | Auto-generated creation time |  |
| **FechaModificacion**<br>`fld4FojYttVnpH0wV` | `lastModifiedTime` | Auto-generated modification time |  |
| **RUTsostenedor**<br>`fldXLjaKZpBcuExA4` | `singleLineText` | Type: singleLineText |  |
| **RUTsostenedorLookup**<br>`fldpAQan44Kr7NRDx` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **sostenedorNombre**<br>`fldZuuoPVt092Wnj0` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **RectorNombre**<br>`fldcqsF55c5brM723` | `singleLineText` | Type: singleLineText |  |
| **colegioRUT**<br>`fld4NQRfbTJs0ZYXf` | `singleLineText` | Type: singleLineText |  |
| **RBD**<br>`fld3yUCOlexLALKub` | `singleLineText` | Type: singleLineText |  |
| **colegioNombre**<br>`fldNg9sxwkQjDnA3e` | `singleLineText` | Type: singleLineText |  |
| **colegioSiglaTag**<br>`fldpjrw7THcbyWzlu` | `singleSelect` | Single choice dropdown | `Pruebas`, `Almondale
  San Pedro`, `Almondale
  Lomas`, `The
  Almondale School Valle`, `Gestión` |
| **colegioEnObservacion**<br>`fld6AhPYSn5w85cdw` | `checkbox` | True/False checkbox |  |
| **colegioCalificaValores**<br>`fldNE2x9HXOsYPb8s` | `number` | Numeric field |  |
| **colegioObsAulaEnCampania**<br>`fldvMbFlfNFZzWNkC` | `number` | Numeric field |  |
| **CantDocentesObservables**<br>`fld76ezIr01iqVCnJ` | `count` | Type: count |  |
| **colegioCantObsAula**<br>`fldIGDWazRuWAg5i3` | `count` | Type: count |  |
| **colegioCantObsAulaCompleta**<br>`fld4RvoJGtlEMAwKy` | `rollup` | Rollup from linked records |  |
| **ConSinObasAula**<br>`fldL5KUfjOWurWLJh` | `formula` | Calculated field | Formula: `IF(
  {fldIGDWazRuWAg5i3}>0,
  "Con",
  "Sin"
...` |
| **colegioCantObsAulaPer1**<br>`fldepKrfJzYrzpwCI` | `rollup` | Rollup from linked records |  |
| **colegioCantObsAulaPer2**<br>`fldDazr1UQg67t6DY` | `rollup` | Rollup from linked records |  |
| **colegioCantObsAulaPer3**<br>`fldndkibQtt464zcd` | `rollup` | Rollup from linked records |  |
| **colegioCantFeedB**<br>`fldDT6b5c0W4bTVqZ` | `count` | Type: count |  |
| **ConSinFEEDB**<br>`fldzBGihLdqNDj9j9` | `formula` | Calculated field | Formula: `IF(
  {fldDT6b5c0W4bTVqZ}>0,
  "Con",
  "Sin"
...` |
| **LogoColegio**<br>`fldPZveSs68RaJR58` | `multipleAttachments` | Type: multipleAttachments |  |
| **colegioComuna**<br>`fldngrqwFwdsoc4zD` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Region**<br>`fldclz3WRpxEBKiqj` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ParamPDF1enOAs**<br>`fld3c7FYi9Erb92Au` | `number` | Numeric field |  |
| **colegioDependencia**<br>`fld5GspuomOQ8CPW2` | `singleSelect` | Single choice dropdown | `Particular Subvencionado`, `Particular pagado` |
| **colegioVulnerabilidadSEP**<br>`fldjxmDHn3AG24q9u` | `singleSelect` | Single choice dropdown | `Emergente` |
| **colegioComputacion**<br>`fldxVxIpA2dHc85jE` | `checkbox` | True/False checkbox |  |
| **colegioLabCiencias**<br>`fld7jrn7pvPN50rMX` | `checkbox` | True/False checkbox |  |
| **colegioComputadoresDisponiblesEstudiantes**<br>`fldzEgBp2mQxwpEoG` | `number` | Numeric field |  |
| **colegioEstCursoPorComputador copy**<br>`fldFeF71YvjIJVuC4` | `formula` | Calculated field | Formula: `IF({fldYV6W6o0jf98FZA}>0,
  {fldzEgBp2mQxwpEoG} /...` |
| **colegioBiblioteca**<br>`fldF7vAZkk56YEeiV` | `checkbox` | True/False checkbox |  |
| **colegioMatriculaPreBasica**<br>`fldMm54Ov2Gnki3dZ` | `number` | Numeric field |  |
| **colegioMatriculaBasica**<br>`fldehsMN2l8CEIq8Q` | `number` | Numeric field |  |
| **colegioMatriculaMedia**<br>`fld7XLP7kFvGSATDl` | `number` | Numeric field |  |
| **colegioMatriculaTotal**<br>`fldE9EVodOBXkcJ08` | `formula` | Calculated field | Formula: `{fldMm54Ov2Gnki3dZ}+
{fldehsMN2l8CEIq8Q}+
{fld7X...` |
| **colegioCantDocentes**<br>`fldLBCCS1FIafrJEp` | `number` | Numeric field |  |
| **colegioCursoMasGrande**<br>`fldYV6W6o0jf98FZA` | `number` | Numeric field |  |
| **colegioEntorno**<br>`fldAiH7QjLuYzWgtu` | `singleSelect` | Single choice dropdown | `Urbano ciudad grande` |
| **colegioMultigrado**<br>`fldFfGB4tRDVVCwhu` | `checkbox` | True/False checkbox |  |
| **colegioSimceLeng**<br>`fld83cP1IayVqxMGk` | `number` | Numeric field |  |
| **colegioSimceLenTxt**<br>`fld6dvaMVDkyXNPCO` | `formula` | Calculated field | Formula: `IF(
  {fld83cP1IayVqxMGk} > 380, "Sobresaliente",...` |
| **colegioSimceMate**<br>`fldrcRNZtCA8XTc4y` | `number` | Numeric field |  |
| **colegioSimceMatTxt**<br>`fldWGq6egcHJPHdBJ` | `formula` | Calculated field | Formula: `IF(
  {fldrcRNZtCA8XTc4y} > 380, "Sobresaliente",...` |
| **colegioPAESLen**<br>`fld0DqRQtJqico0ZZ` | `number` | Numeric field |  |
| **colegioPAESLenTxt**<br>`fld7lqbQqcxruaxOS` | `formula` | Calculated field | Formula: `IF(
  {fld0DqRQtJqico0ZZ} > 800, "Sobresaliente",...` |
| **colegioPAESMate**<br>`fldR7DDFsqjf7vMB0` | `number` | Numeric field |  |
| **colegioPAESMatTxt**<br>`fldQiHJuO89QkUF1D` | `formula` | Calculated field | Formula: `IF(
  {fldR7DDFsqjf7vMB0} > 800, "Sobresaliente",...` |
| **colegioPerfil**<br>`fldR6FiU9ryMTSH8S` | `formula` | Calculated field | Formula: `" Mi colegio se ubica en la región "&T({fldclz3WRp...` |
| **colegioAntiguedad**<br>`fld844uxz1fsqMJUx` | `number` | Numeric field |  |
| **colegioSuperiorEntrevistasFEEDB**<br>`fld66fCOFnRZvOovA` | `email` | Email address |  |
| **Estudiantes**<br>`fldFyzwDayEQiqMHO` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ObservacionesAula**<br>`fldCfAG8rriVlI9uh` | `singleLineText` | Type: singleLineText |  |
| **ObservacionesAula copy**<br>`fldeSOP5Jemsxw8Ow` | `singleLineText` | Type: singleLineText |  |
| **ObservacionesAula 2**<br>`fldpTIyE8qO5EN2SD` | `singleLineText` | Type: singleLineText |  |
| **Docentes**<br>`fld4RYf7SKPf2GUTT` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ObservacionesAula 3**<br>`fldM7rRAg4Lt7qZ1g` | `singleLineText` | Type: singleLineText |  |
| **ObservacionesAula 4**<br>`fld4WkrmZyqv0LH9s` | `singleLineText` | Type: singleLineText |  |

---

## 📋 8. ComunasRegiones

*Table ID: `tbl0OBFebUTNMwIdi`*
*Fields: 4*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Comuna**<br>`fldcRcNBPGIbvhyVK` | `singleLineText` | Type: singleLineText |  |
| **Region**<br>`fld9jN5P30cSSsMZ2` | `singleSelect` | Single choice dropdown | `Arica y Parinacota`, `Tarapacá`, `Antofagasta`, `Atacama`, `Coquimbo` *(+11 more)* |
| **Colegios**<br>`fld8Nbn2kYK8xEzla` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Marca**<br>`flddUyGAu58HG8lMS` | `singleLineText` | Type: singleLineText |  |

---

## 📋 9. Curriculum

*Table ID: `tblIH6HfaK31GX3aM`*
*Fields: 45*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **OA**<br>`fldiEBi8B4MdGizjQ` | `singleLineText` | Type: singleLineText |  |
| **versionTablaCurriculum**<br>`fldxlqAUdiVf4joNh` | `singleLineText` | Type: singleLineText |  |
| **OAaxis**<br>`fld4mrmhib8sEKa6U` | `formula` | Calculated field | Formula: `SWITCH(
  {fldWU0YUchMfjr8b3},
  'Medición', 'Me...` |
| **EjeTag**<br>`fldWU0YUchMfjr8b3` | `singleSelect` | Single choice dropdown | `Escritura - Producción`, `Datos y probabilidades`, `Lectura - Comprensión`, `Comunicación oral`, `Investigación` *(+16 more)* |
| **OAdescripcion**<br>`fld6HE1DA3CvtMnRa` | `multilineText` | Multi-line text |  |
| **FlagTraducirEN**<br>`fldmhJa8WDpNfUPZ0` | `number` | Numeric field |  |
| **OAdescripcionEN**<br>`fldXGcMZeWwtwqFI7` | `multilineText` | Multi-line text |  |
| **TraductorModelo**<br>`fldSB7MVzaCJMQgH9` | `singleLineText` | Type: singleLineText |  |
| **OAdescripcionResumen**<br>`fldqCeoltAnWP5Pow` | `aiText` | Type: aiText |  |
| **RevisarConPAES**<br>`fld8HHZZvsoMVIQsP` | `number` | Numeric field |  |
| **PAES_M1**<br>`fldUqerwcal4K7SPh` | `singleLineText` | Type: singleLineText |  |
| **HAB_PAES_M1**<br>`fldR7qMftuH7GM7ht` | `singleLineText` | Type: singleLineText |  |
| **OAtipo**<br>`fldXuldhod6XKlXda` | `singleLineText` | Type: singleLineText |  |
| **Respaldo_Pertinencia_PAES_M1**<br>`fldvAQeoy9D1fiaPW` | `multilineText` | Multi-line text |  |
| **Version2005**<br>`fldCIdRuQYsde2Zfz` | `singleLineText` | Type: singleLineText |  |
| **Fecha2005**<br>`fldHsqi6RYZslu99J` | `singleLineText` | Type: singleLineText |  |
| **IdentificarHabilidadesFlag**<br>`fldLNL26IkpVf04Hc` | `number` | Numeric field |  |
| **Habilidad_Paes_M1**<br>`fldlkSl2CVvBt3hkp` | `singleLineText` | Type: singleLineText |  |
| **Respaldo_Habilidades_PAES_M1**<br>`fldrmt1cDUatMtr1S` | `multilineText` | Multi-line text |  |
| **Version2006**<br>`fldOfjT2ypBcQBPNG` | `singleLineText` | Type: singleLineText |  |
| **Fecha2006**<br>`fldJOpRhi7UZnHLql` | `singleLineText` | Type: singleLineText |  |
| **Prompt**<br>`fldf8cLrn7cKpErNe` | `singleLineText` | Type: singleLineText |  |
| **FechaUltimaIA**<br>`fldS0r2VZ5Xw9ffue` | `singleLineText` | Type: singleLineText |  |
| **Materia**<br>`fldPnTPYo5AWnQASM` | `singleLineText` | Type: singleLineText |  |
| **MateriaTag**<br>`fldgEt903CiF3WtSt` | `singleSelect` | Single choice dropdown | `Comprensión lectora`, `Matemática`, `Historia y Geografía`, `Ciencias`, `Materia` |
| **Eje**<br>`fldR3vKixBl7aYYXq` | `singleLineText` | Type: singleLineText |  |
| **OAnivel**<br>`fldElXH6hTJdXHoox` | `singleLineText` | Type: singleLineText |  |
| **OAnivelTxt**<br>`fldwguqL5AyGgz48s` | `formula` | Calculated field | Formula: `SWITCH({fldElXH6hTJdXHoox},"5",'5° Básico',"6",'6°...` |
| **OAnivelTxtTag**<br>`fldkxuK61hTh77sDk` | `singleSelect` | Single choice dropdown | `5° Básico`, `6° Básico`, `7° Básico`, `8° Básico` |
| **OaAntiguedad**<br>`fldlVwKIoa2ZMaeVw` | `formula` | Calculated field | Formula: `VALUE(MID({fldiEBi8B4MdGizjQ},3,2)&RIGHT({fldiEBi8...` |
| **RutaEstudiante**<br>`fldq2FBqRDsPQ0bXD` | `singleLineText` | Type: singleLineText |  |
| **OAsNoLogradosMA**<br>`fldmKTf8yvuL5kxLN` | `singleLineText` | Type: singleLineText |  |
| **RutaEstudiante 2**<br>`fldKWyzzF8GiisLRZ` | `singleLineText` | Type: singleLineText |  |
| **RutaEstudianteHistorica**<br>`fldkAGdPLJCJFPvgS` | `singleLineText` | Type: singleLineText |  |
| **OAsNoLogradosMA 2**<br>`fldEawbBVh1tu7FU5` | `singleLineText` | Type: singleLineText |  |
| **OasPendientesPorEstudiante 6**<br>`fldyKL0PSNURWz5ir` | `singleLineText` | Type: singleLineText |  |
| **PreguntasDiagnostico**<br>`fldzNm79cH4bJ9AqF` | `singleLineText` | Type: singleLineText |  |
| **OAEnPreguntasDiagnostico**<br>`fldYq3d703EBsEmTh` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **CantPreguntasDiagnosticoValida1**<br>`fldRaPmpbgtcgS57w` | `count` | Type: count |  |
| **OAsPendientesPorEstudiante**<br>`fldqlQ4HYQeAUMXhT` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **PreguntasDiagnostico 2 copy**<br>`fldtUTADPBULZBiUn` | `singleLineText` | Type: singleLineText |  |
| **OAsPendientesPorEstudiante copy**<br>`fld9EQsEsqaURXWkC` | `singleLineText` | Type: singleLineText |  |
| **BancoActividades**<br>`fld84fFj2WCVpOsiO` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **OAsNoLogradosMA 2 copy**<br>`fldr4BP1oB0NsWzgL` | `singleLineText` | Type: singleLineText |  |
| **RespuestasDiagnostico2**<br>`fldUnHKbVVvtP7NvZ` | `singleLineText` | Type: singleLineText |  |

---

## 📋 10. Cursos

*Table ID: `tblUG7oNETrFF0Hi7`*
*Fields: 4*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Curso**<br>`fldIcplTGwEvaoI4g` | `singleLineText` | Type: singleLineText |  |
| **Matricula**<br>`fldMpiJbZhNDDLrvN` | `number` | Numeric field |  |
| **Damas**<br>`flduujUMIGSYUKTxx` | `number` | Numeric field |  |
| **Varones**<br>`fldSM3LNOQTEkZNX6` | `number` | Numeric field |  |

---

## 📋 11. DEMRE_HISTORICO

*Table ID: `tblIMFYv2br167xsO`*
*Fields: 25*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Rec**<br>`fldgdzLPP3TMaMUvw` | `autoNumber` | Type: autoNumber |  |
| **VersionForm**<br>`fldgZV8fJJSxNj9tU` | `singleLineText` | Type: singleLineText |  |
| **AnnoProceso**<br>`fld0d6jsPe12uaBHD` | `number` | Numeric field |  |
| **FechaAplicacion**<br>`fld0bDWXvyKkHe66o` | `date` | Date |  |
| **Prueba**<br>`fld4Qws8tE5KJJBs9` | `singleSelect` | Single choice dropdown | `Historia y Cs. Sociales`, `Matemática M1`, `Cs. Biología`, `Cs. Física`, `Cs. Química` *(+5 more)* |
| **Materia**<br>`fldnxl1tUZzkMgo2B` | `singleLineText` | Type: singleLineText |  |
| **TipoPrueba**<br>`flduqFntvwrMMowtm` | `singleSelect` | Single choice dropdown | `Regular`, `Invierno`, `Tipo de Prueba` |
| **Forma**<br>`fld6LhoWydA3RpuxC` | `singleLineText` | Type: singleLineText |  |
| **NombrePrueba**<br>`fldjqgo3UAlsGgCdx` | `singleSelect` | Single choice dropdown | `PSU`, `TRANSICIÓN`, `PAES`, `Prueba` |
| **Eje**<br>`fldrN5Df2ADOsd48Z` | `singleSelect` | Single choice dropdown | `Eje` |
| **NumPregunta**<br>`fldxnZuLW7oYtyOvt` | `number` | Numeric field |  |
| **RptaDEMRE**<br>`fldxdgBlhyaq2PYRm` | `singleLineText` | Type: singleLineText |  |
| **Texto_txt**<br>`fldwMaGlgysFbBNh9` | `multilineText` | Multi-line text |  |
| **Pregunta_txt**<br>`fldjTIugmhbpTgtHN` | `multilineText` | Multi-line text |  |
| **RespuestaCorrecta**<br>`fldu5esOxmoYKgfGx` | `singleLineText` | Type: singleLineText |  |
| **RespuestaCorrectaSeguridad**<br>`fldZSQes0mqvE42Q8` | `singleLineText` | Type: singleLineText |  |
| **RespuestaCorrectaJustificacion**<br>`fldgU2wlpO1t7m6xH` | `multilineText` | Multi-line text |  |
| **RespuestaCorrecta_Modelo**<br>`fldwIuMCOnWISdlHh` | `singleLineText` | Type: singleLineText |  |
| **RespuestaCorrecta_Fecha**<br>`fldD1FEa2fIdeitcy` | `singleLineText` | Type: singleLineText |  |
| **RespuestaCorrecta_Version1010**<br>`fldP4m6wppbt4iFhX` | `singleLineText` | Type: singleLineText |  |
| **RespuestaCorrecta_Procesado**<br>`fldhbnFUxZpTE8CQa` | `number` | Numeric field |  |
| **Creado**<br>`fld1467rnzVGje3J2` | `createdTime` | Auto-generated creation time |  |
| **ValidarRptas**<br>`fldAA3SNK337Weute` | `formula` | Calculated field | Formula: `IF(
  {fldxdgBlhyaq2PYRm} = {fldu5esOxmoYKgfGx}, ...` |
| **ValidaNumPregunta**<br>`fldR7x7A6gMw4XUSK` | `formula` | Calculated field | Formula: `IF(
  LEN(T({fldxnZuLW7oYtyOvt}))=1,
  IF(LEFT({...` |
| **VALIDADA**<br>`fldvxaiCFQLm3fEB7` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldhbnFUxZpTE8CQa}=9,
    {fldA...` |

---

## 📋 12. Docentes

*Table ID: `tbllI8vlFVPDYjzXq`*
*Fields: 96*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTdocente**<br>`fld8Gt06jdpc6ejVv` | `singleLineText` | Type: singleLineText |  |
| **DocentePaterno**<br>`fldXyZDfCqXyadr7Q` | `singleLineText` | Type: singleLineText |  |
| **DocenteMaterno**<br>`fldU56HyPLWh43lKC` | `singleLineText` | Type: singleLineText |  |
| **DocenteNombres**<br>`fldinXY1mUDJEdjqt` | `singleLineText` | Type: singleLineText |  |
| **DocenteDepartamento**<br>`fldbHn8kTlqs8fyRP` | `singleLineText` | Type: singleLineText |  |
| **ColegioPrincipal**<br>`fldq4TNo8in3jG7ik` | `singleSelect` | Single choice dropdown | `Pruebas`, `Almondale San Pedro`, `Almondale Lomas`, `The Almondale School Valle`, `Gestion Almondale` |
| **DocenteEmail**<br>`flduWPBOvIpuxwKA6` | `email` | Email address |  |
| **NombreCompletoURLA010**<br>`fld9nPi1udB3jvOqs` | `formula` | Calculated field | Formula: `IF({fldwqw6lTfEm5K5n9}!="",
SUBSTITUTE(
  SUBSTI...` |
| **GrupoSoftr**<br>`fldY8UsdpM3ityEo2` | `singleLineText` | Type: singleLineText |  |
| **DocenteCargo**<br>`fldsrfPACX60BgMv6` | `singleLineText` | Type: singleLineText |  |
| **CantObsAula**<br>`fldtdkjt78UBYq7cW` | `count` | Type: count |  |
| **CantObsAula-TS2**<br>`fldXQL0NqPasfPdEY` | `count` | Type: count |  |
| **CantEntrevistas**<br>`fldvEKOkP3aF89QgG` | `count` | Type: count |  |
| **ObservadoAula**<br>`fld1D9iED1DSFowdI` | `checkbox` | True/False checkbox |  |
| **EvaluadorAula**<br>`fldXt71n4VQtIAfDF` | `checkbox` | True/False checkbox |  |
| **DocenteNombreCompleto**<br>`fldwqw6lTfEm5K5n9` | `formula` | Calculated field | Formula: `TRIM({fldXyZDfCqXyadr7Q}) &' '& TRIM({fldU56HyPLWh...` |
| **DocenteNombreCompletoTag**<br>`fldDxdLjUqB4amCeW` | `singleSelect` | Single choice dropdown | `Alonso Araya Lorena`, `Alonso Rodríguez Laura`, `Araya Gómez José`, `Bustamante Fuentes Alejandro`, `Bustamante Muñoz Jimena` *(+405 more)* |
| **JefaturaCurso**<br>`fldzK3fUFUeWsVH9T` | `singleLineText` | Type: singleLineText |  |
| **HaceIngles**<br>`fldqdr3cFctnTWHNl` | `checkbox` | True/False checkbox |  |
| **DocentePrioritario**<br>`fldI3hfFSELsDn482` | `checkbox` | True/False checkbox |  |
| **ColegioPrincipalTxt**<br>`fld5sFFZSnNzA6SmT` | `singleSelect` | Single choice dropdown | `San Pedro`, `Lomas`, `Valle`, `Pruebas`, `Colegio` *(+5 more)* |
| **ColegioLookUp**<br>`fldl0UZevx8uZT0zk` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EmitePDF1**<br>`fld1crDTRwgcIUYWm` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **CantDocentesObservables**<br>`flduwh4A0VTIsSlpy` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **superiorFEEDBemail**<br>`fldIccJAIfyD6Tkhh` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioEnObservacion**<br>`fldRZhjMJiZXkQ3uF` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioSostenedorNombre**<br>`fldHjzZvC5dh3XaNF` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioRBD**<br>`fldmCEPYiTOyrUyKc` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioLogo**<br>`fldiGPteqEReZcBU7` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioRector**<br>`fldEpnhda0iM0FyKU` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioRegion**<br>`flddiQa0qYCICpyVs` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioComuna**<br>`fldUgDBYRPVzTODyw` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioFlag1**<br>`fldHQ36tPaL45fSi8` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioFlag2**<br>`fldjZ70MKXi7oPPWU` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Colegio2**<br>`fldeVfBwtNgutCGXX` | `singleLineText` | Type: singleLineText |  |
| **Colegio3**<br>`fldnsTh7r2gwpbaGN` | `singleLineText` | Type: singleLineText |  |
| **DocenteTrato**<br>`fldmYY1YyS4g1TIoh` | `singleSelect` | Single choice dropdown | `Sra.`, `Srta.`, `Sr.`, `doña`, `don` *(+1 more)* |
| **DocenteSexo**<br>`fld9IG6WDgiskPEje` | `singleLineText` | Type: singleLineText |  |
| **DocenteFechaNacimiento**<br>`fldSm8OHBEqIRg12z` | `date` | Date |  |
| **DocenteFechaIngreso**<br>`fldJcecGwhFN3rdQc` | `date` | Date |  |
| **DocenteAnioIngreso**<br>`fldl37Af7Ls5oU5H5` | `formula` | Calculated field | Formula: `IF(
  {fldJcecGwhFN3rdQc}!="",
  YEAR({fldJcecGw...` |
| **DocenteAnioIngresoTag**<br>`fldE5eVYZwUxe64xU` | `singleSelect` | Single choice dropdown |  |
| **DocenteAntiguedad**<br>`flditUIf0Vk8De7Ly` | `formula` | Calculated field | Formula: `IF({fldJcecGwhFN3rdQc}!="",
  DATETIME_DIFF(TODAY...` |
| **DocenteExperienciaAnnos**<br>`fldhMiPWITh8NOqwc` | `number` | Numeric field |  |
| **DocenteEdad**<br>`fldKXhGzzv6nWpctr` | `formula` | Calculated field | Formula: `IF({fldSm8OHBEqIRg12z}!="",
  DATETIME_DIFF(TODAY...` |
| **DocenteResumenObsAulas**<br>`fldGmPlS39Sez9k2l` | `multilineText` | Multi-line text |  |
| **DocenteAcuerdosObsAulasAnterior**<br>`fldFFoGvNOOVZSZVh` | `multilineText` | Multi-line text |  |
| **DocenteEvaluadorObsAulasAnterior**<br>`fldBFWR18MF7RZu4h` | `singleLineText` | Type: singleLineText |  |
| **DocenteUrgenciaObsAulasAnterior**<br>`fld00DA3g1Uv3XU68` | `singleLineText` | Type: singleLineText |  |
| **DocenteEjeObsAulasAnterior**<br>`fldogyoCEKCF8wbQO` | `singleLineText` | Type: singleLineText |  |
| **ModificadosEntrevAnterior**<br>`fldmJT1xJxftITUQV` | `lastModifiedTime` | Auto-generated modification time |  |
| **FechaUltimaObsAulaStr**<br>`fldrYLuDvpTSUTs7m` | `formula` | Calculated field | Formula: `IF({fldmJT1xJxftITUQV}!="",
  DATETIME_FORMAT({fl...` |
| **DesempenoPromedio**<br>`fldR7XreK3KFhaYTt` | `formula` | Calculated field | Formula: `{fld9QQTxdwxJzwGQN}+
{fldY4jzXr34czAvl7}+
{fldao...` |
| **SortPorDesemPromedio**<br>`fldVCer7j7wHDcmEb` | `number` | Numeric field |  |
| **PROMEDIO-ACADEMICO**<br>`fld5hoyy0Tk87vT0Y` | `rollup` | Rollup from linked records |  |
| **PROMEDIO-SOCIOEMOCIONAL**<br>`fldvSLMDosAer8yVq` | `rollup` | Rollup from linked records |  |
| **ClasesPerfectas**<br>`fld9QQTxdwxJzwGQN` | `count` | Type: count |  |
| **ClasesBuenas**<br>`fldY4jzXr34czAvl7` | `count` | Type: count |  |
| **ClasesBasicas**<br>`fldaor5NNjmLhoNDN` | `count` | Type: count |  |
| **ClasesInsatisfactorias**<br>`fldlMviOgjGnVwJ8o` | `count` | Type: count |  |
| **ObsAulaCompletas**<br>`fldNKo5UVLazpbNn3` | `count` | Type: count |  |
| **CantObsAula-T1**<br>`fldTukuWAuQTHYo93` | `count` | Type: count |  |
| **CantObsAula-T2**<br>`fldp9HoBJTVn1I3s7` | `count` | Type: count |  |
| **CantObsAula-T3**<br>`fldXqr5Vk3lRJhDP2` | `count` | Type: count |  |
| **ObservacionesAula**<br>`fldARLY79XEToroC8` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ObservacionesAula copy**<br>`fldEr2V83zTMDQCqP` | `singleLineText` | Type: singleLineText |  |
| **ObservacionesAula copy 2**<br>`fld87gMPnaYSXLW7u` | `singleLineText` | Type: singleLineText |  |
| **miniExtensions**<br>`fldtNynuwPAOUA4A2` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Manual sort**<br>`fldZvSs5dI540QTvY` | `manualSort` | Type: manualSort |  |
| **ObservacionesAula 2**<br>`fld1UEb8iTdbu7yQf` | `singleLineText` | Type: singleLineText |  |
| **URL_Prefill_A010_Compuesta**<br>`fldQWReUK5IjXc6N1` | `formula` | Calculated field | Formula: `"https://form.jotform.com/251688711542663?rut="&{f...` |
| **URL_Prefill_A010_ENCODED**<br>`fld6pQdQDWLv32QyP` | `formula` | Calculated field | Formula: `ENCODE_URL_COMPONENT({fldQWReUK5IjXc6N1})` |
| **URL_Prefill_A010_Embedded**<br>`flduGjNhY2Fxevyc6` | `formula` | Calculated field | Formula: `"/Form-ObservacionAula?url="&{fld6pQdQDWLv32QyP}` |
| **AnteriorFechaDia**<br>`fld74y6yUJNPaWBUJ` | `formula` | Calculated field | Formula: `IF({fldrYLuDvpTSUTs7m}!="",
  IF(
    LEFT({fldr...` |
| **AnteriorFechaMes**<br>`fldJc9RRax1kMZ8lh` | `formula` | Calculated field | Formula: `IF({fldrYLuDvpTSUTs7m}!="",
    MID({fldrYLuDvpTS...` |
| **AnteriorFechaAnio**<br>`fldcRdToGPfydRUwa` | `formula` | Calculated field | Formula: `IF({fldrYLuDvpTSUTs7m}!="",
    RIGHT({fldrYLuDvp...` |
| **URLA010_Colegio**<br>`fldxdhiGyp5CTuZbk` | `formula` | Calculated field | Formula: `SWITCH({fldq4TNo8in3jG7ik},
  "Almondale San Pedr...` |
| **URLA010_DocenteEvaluadorObsAulasAnterior**<br>`fldGyn1DljneMpPIN` | `formula` | Calculated field | Formula: `SUBSTITUTE(
  SUBSTITUTE({fldBFWR18MF7RZu4h}," ",...` |
| **URLA010_UrgenciaAnterior**<br>`fldcMqdVJWl4MLyNB` | `formula` | Calculated field | Formula: `SUBSTITUTE(
  SUBSTITUTE({fld00DA3g1Uv3XU68}," ",...` |
| **URLA010_AcuerdosAnterior**<br>`fldmM12VX7a1jwe1l` | `formula` | Calculated field | Formula: `SUBSTITUTE(
  SUBSTITUTE({fldFFoGvNOOVZSZVh}," ",...` |
| **URLA010_EjeAnterior**<br>`fldcbr3aRDqOdCn9s` | `formula` | Calculated field | Formula: `SUBSTITUTE(
  SUBSTITUTE({fldogyoCEKCF8wbQO}," ",...` |
| **Docentes-mes**<br>`fldCIOKyRvzq4VTUi` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Docentes-mes copy**<br>`fldOrH8oLZVYgiJly` | `singleLineText` | Type: singleLineText |  |
| **CantObsAula-TS3**<br>`fldsPnI9iG7y1kBWq` | `count` | Type: count |  |
| **CantEntr-TS1**<br>`flddRc3H9Xs7og0hG` | `count` | Type: count |  |
| **CantEntr-TS3**<br>`fld62uNm9Cr9m8rtL` | `count` | Type: count |  |
| **CantEntr-TS2**<br>`fldBmmHHUZFlHKsx2` | `count` | Type: count |  |
| **PROM-ACAD-TS1**<br>`fldJIl2GRIO64aHEq` | `rollup` | Rollup from linked records |  |
| **PROM-ACAD-TS3**<br>`fldxliV0bNuXbBgC2` | `rollup` | Rollup from linked records |  |
| **PROM-ACAD-TS2**<br>`fldGoUgkmnmotG7UE` | `rollup` | Rollup from linked records |  |
| **CantObsAula-TS1**<br>`fldREGVdcd6iKYaQK` | `count` | Type: count |  |
| **PpObsAula-TS2**<br>`fldD507LSMQeI8MOi` | `formula` | Calculated field | Formula: `IF(
  {fldXQL0NqPasfPdEY}>0,
  ROUND({fldXQL0NqP...` |
| **PpObsAula-TS1**<br>`fld2GC1Fd9fqwdjsY` | `formula` | Calculated field | Formula: `IF(
  {fldREGVdcd6iKYaQK}>0,
  ROUND({fldREGVdcd...` |
| **PpObsAula-TS3**<br>`fldgY3IWnfczk9YNK` | `formula` | Calculated field | Formula: `IF(
  {fldsPnI9iG7y1kBWq}>0,
  ROUND({fldsPnI9iG...` |
| **PpCONObsAulaAlaFecha**<br>`fldoEvwd2JHkDc1EE` | `formula` | Calculated field | Formula: `IF(
  {fldtdkjt78UBYq7cW}>0,
  ROUND({fldtdkjt78...` |
| **PpSINObsAulaAlaFecha**<br>`fldBXO6aEmn6JQ6gq` | `formula` | Calculated field | Formula: `IF({fldtdkjt78UBYq7cW}=0,
IF({flduwh4A0VTIsSlpy}>...` |

---

## 📋 13. Docentes-mes

*Table ID: `tblq1XtL97d8BsFTv`*
*Fields: 17*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTdocente**<br>`fldMRwM8B82QakJ7s` | `singleLineText` | Type: singleLineText |  |
| **RUTloopUp**<br>`fldfQViLs893qaK09` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **SeObservaAula**<br>`fldeXeu9KHCogsqa6` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **DocenteNombre**<br>`fld6AwBVYHfa5KTVY` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **DocentePrioritario**<br>`fldn1yAmaK6TuXouq` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Annio**<br>`fld3JSdENxdtghjkC` | `number` | Numeric field |  |
| **Mes**<br>`fldzf8s6SFL5EskCI` | `number` | Numeric field |  |
| **TrimestreSemestre**<br>`fldgSBVByAkKnWJ1v` | `number` | Numeric field |  |
| **Observaciones**<br>`fldcesHVNUonxI0Vh` | `number` | Numeric field |  |
| **Entrevistas**<br>`fldBbr0cO2H5elFCW` | `number` | Numeric field |  |
| **Desempennio**<br>`fldajKaWeMNwgsLPx` | `number` | Numeric field |  |
| **Academico**<br>`fldxkCaTMRJuEtmOS` | `number` | Numeric field |  |
| **SocioEmocional**<br>`fldDETnFyhqBt76zH` | `number` | Numeric field |  |
| **ClasesPerfectas**<br>`fld4oVJC8vDl62YON` | `number` | Numeric field |  |
| **ClasesBuenas**<br>`fldIyBXSiRCHN2bT7` | `number` | Numeric field |  |
| **ClasesBásicas**<br>`fldjiYqKf0PSo7ma0` | `number` | Numeric field |  |
| **ClasesInsatisfactorias**<br>`fld3ZPNAjDcRNlmbQ` | `number` | Numeric field |  |

---

## 📋 14. Estudiantes

*Table ID: `tblwHXL65O8enTvyC`*
*Fields: 236*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **estudianteRut**<br>`fldVJavBySnz5OTvm` | `singleLineText` | Type: singleLineText |  |
| **FechaCreacionEstudiante**<br>`fld92kavfC5NYuR6T` | `createdTime` | Auto-generated creation time |  |
| **estudianteColegio**<br>`fldFp8a8i6wQkyHMB` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **colegioNombre**<br>`fldyesZnPwxrvo25q` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioSigla**<br>`fldSh3WZPkk5sCQaj` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioComuna**<br>`fldbY0WuiFxSu8wz5` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioRegion**<br>`fldDWDKzAJro8Tqh5` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioDependencia**<br>`fldO7Pg7Jp86aIj2c` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioVulnerabilidadSEP**<br>`fldCpVNWlEbXZpteP` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioEstudiantesPorComputador**<br>`fldK7nMrFaunCts0L` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioLaboCiencias**<br>`fldXnpQ6pHIx3qi9Q` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioEntornoUrbano**<br>`fldpcTfvZOALWSG3P` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioMultigrado**<br>`fldLg6HRiIireqOHz` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioSimceLeng**<br>`fld6iAGxCFrBhrwuO` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioSimceMate**<br>`fldkDXiTJamwhkAhQ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioPAESLeng**<br>`fldTmYfHG7pzNGBOJ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioPAESMatem**<br>`fldq0Pl7Lz4UVWaCw` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ApodRUT**<br>`fldlBFAl2f19aOBvj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ApodNombreCompleto**<br>`fldI1UHc0W5pXuOeG` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ApodEmail**<br>`fldQh7TvuDMTmU5F7` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ApodCuadrante**<br>`fldqbDEiLQUFgBZSK` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ApodCuadranteTipoInput**<br>`fldVBubI4gdRHVveQ` | `number` | Numeric field |  |
| **ApodCuadranteLiderInput**<br>`fldYOTJEn1WwiUs2r` | `number` | Numeric field |  |
| **CreadoUsuariosWeb**<br>`fldEZ9WltE7TXfO0Q` | `number` | Numeric field |  |
| **PasswordUsuariosWeb**<br>`fldL8bVLMWrkvSGSs` | `formula` | Calculated field | Formula: `{fldVJavBySnz5OTvm} & {fldXv16hfto3nmNJg} & MONTH(...` |
| **CantTareas**<br>`fldnYEXzHbR8qScb5` | `count` | Type: count |  |
| **AvisoMisTareas**<br>`fld6Fg2QyaodDiIxG` | `singleLineText` | Type: singleLineText |  |
| **estudiantesMOT**<br>`fld0UMMOpBMiWKeCZ` | `number` | Numeric field |  |
| **estudiantesINT**<br>`fldnVPSkbOEITiinC` | `number` | Numeric field |  |
| **estudiantesTIN**<br>`fldKDYHNzVj6n4Vcq` | `number` | Numeric field |  |
| **5LE**<br>`fldlpzsHiKf8kUctH` | `number` | Numeric field |  |
| **6LE**<br>`fldeHHzno6meDZI7Y` | `number` | Numeric field |  |
| **7LE**<br>`fldmQboF1Uyxl77ha` | `number` | Numeric field |  |
| **8LE**<br>`fldla4G0gk9pxNRzx` | `number` | Numeric field |  |
| **9LE**<br>`fldFngasSxDEjjcNK` | `number` | Numeric field |  |
| **10LE**<br>`fldjy6SGIG3doqBtL` | `number` | Numeric field |  |
| **5MA**<br>`fld1SzgfhHwvxxvPL` | `number` | Numeric field |  |
| **6MA**<br>`fldujCTITW5Lxs17l` | `number` | Numeric field |  |
| **7MA**<br>`fldYJAQ5kI4OXBxKG` | `number` | Numeric field |  |
| **8MA**<br>`fldt7uaW69fE2dtt5` | `number` | Numeric field |  |
| **9MA**<br>`flddX3iW4stMuIZwa` | `number` | Numeric field |  |
| **10MA**<br>`fldVerjZwD5DL3O9h` | `number` | Numeric field |  |
| **5HG**<br>`fldY0Y9bdNDodv3S9` | `number` | Numeric field |  |
| **6HG**<br>`fldTUFwzJEzt8SRmQ` | `number` | Numeric field |  |
| **7HG**<br>`fldtEEbYFW1CeWCBT` | `number` | Numeric field |  |
| **8HG**<br>`fldMqsCjNXM4DrcFG` | `number` | Numeric field |  |
| **9HG**<br>`flduukOyZ4lllqxu1` | `number` | Numeric field |  |
| **10HG**<br>`fldS7lN8LfI4vo9Ph` | `number` | Numeric field |  |
| **5CS**<br>`fld1Wv09783Y19qNc` | `number` | Numeric field |  |
| **6CS**<br>`fldi1WmpzZHKwZ03V` | `number` | Numeric field |  |
| **7CS**<br>`fldeH97JVFnFjdNtR` | `number` | Numeric field |  |
| **8CS**<br>`flda57w2nX2Kbqw5F` | `number` | Numeric field |  |
| **9CS**<br>`fldx1UWBOXFpkroRf` | `number` | Numeric field |  |
| **10CS**<br>`fldbmhSLAcBEajcPv` | `number` | Numeric field |  |
| **RUTlookUp**<br>`fldlrpTrBULKwnNuA` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **estudianteSexo**<br>`fldwSWTEPW39NRwll` | `singleLineText` | Type: singleLineText |  |
| **FechaNacimiento**<br>`fldSccr8hzuTLlBBP` | `date` | Date |  |
| **estudianteEdad**<br>`fldZFmRFiqfCTkNXK` | `formula` | Calculated field | Formula: `DATETIME_DIFF(TODAY(),{fldSccr8hzuTLlBBP},'years')` |
| **estudianteFoto**<br>`flddMM0830i0AGFpK` | `multipleAttachments` | Type: multipleAttachments |  |
| **estudianteNombre**<br>`fldsa5ZtJ4i6FDCOH` | `singleLineText` | Type: singleLineText |  |
| **estudiantePaterno**<br>`fldVWYhTna7gzDm1O` | `singleLineText` | Type: singleLineText |  |
| **estudianteMaterno**<br>`fldXv16hfto3nmNJg` | `singleLineText` | Type: singleLineText |  |
| **estudianteNombreCompleto**<br>`fldceUdfAqVAOEb5M` | `formula` | Calculated field | Formula: `{fldVWYhTna7gzDm1O}&' '&{fldXv16hfto3nmNJg}&", "&{...` |
| **MisTareasInicialesCreadas**<br>`fldVAx5jfxRPPC0sg` | `number` | Numeric field |  |
| **FechaMisTareasInicialesCreadas**<br>`fld4S7vmKT3j3BJzF` | `singleLineText` | Type: singleLineText |  |
| **version0020**<br>`fldwCfF92rge0fp8N` | `singleLineText` | Type: singleLineText |  |
| **TIPOINT_1**<br>`fldEuqwXl69m85DJu` | `singleLineText` | Type: singleLineText |  |
| **TIPOINT_1_nombre**<br>`fldHbIYoqRvJmhilD` | `formula` | Calculated field | Formula: `SWITCH({fldEuqwXl69m85DJu},"LI","Lingüística","LM"...` |
| **TIPOINT_2**<br>`fldj1X1nwj5Xv97lu` | `singleLineText` | Type: singleLineText |  |
| **TIPOINT_2_nombre**<br>`fldXm1KZtgQ3fhMh1` | `formula` | Calculated field | Formula: `SWITCH({fldj1X1nwj5Xv97lu},"LI","Lingüística","LM"...` |
| **TIPOINT_DEVSTD**<br>`fld8nkvN0pafqPsbB` | `number` | Numeric field |  |
| **TIPOINT_AUTOEVALUADA**<br>`flduPrYyrNsOUZKTE` | `singleLineText` | Type: singleLineText |  |
| **Mot_Reconocimiento**<br>`fld0XXtuWeUK661aJ` | `number` | Numeric field |  |
| **Mot_LogroPersonal**<br>`fld3ILfLQ5FTymoAT` | `number` | Numeric field |  |
| **Mot_Curiosidad**<br>`flduNPrZLIYSz59k8` | `number` | Numeric field |  |
| **Mot_InteresPractico**<br>`fldo0puqPyAcu6u2d` | `number` | Numeric field |  |
| **Mot_RelacionesSociales**<br>`fldz3refThxm2kSYl` | `number` | Numeric field |  |
| **Mot_Autonomia**<br>`fldDq3QRhVwkAbPoP` | `number` | Numeric field |  |
| **Mot_Competividad**<br>`fldAMtFfBGNB7FejS` | `number` | Numeric field |  |
| **Mot_Mayor**<br>`fldTAn707am4ju1Y6` | `formula` | Calculated field | Formula: `IF({fld0XXtuWeUK661aJ}+
   {fld3ILfLQ5FTymoAT}+
...` |
| **Total_Amotivacion**<br>`fldsUjUwpuEsXIhpO` | `number` | Numeric field |  |
| **Mot_PRINCIPAL**<br>`fldy3i0Il590noE5t` | `formula` | Calculated field | Formula: `IF(
  {fldTAn707am4ju1Y6}={fld0XXtuWeUK661aJ},"Re...` |
| **Aficion1raw**<br>`fld4ng9y3AJuYTyVW` | `singleLineText` | Type: singleLineText |  |
| **Aficion2raw**<br>`fldINTvXr5sCeGo9U` | `singleLineText` | Type: singleLineText |  |
| **Aficion3raw**<br>`fldmWAr9TZQAsYKC3` | `singleLineText` | Type: singleLineText |  |
| **Aficion4raw**<br>`flda5AWB7isX6WyNp` | `singleLineText` | Type: singleLineText |  |
| **Aficion5raw**<br>`fldCEVxqCHKJkHmNJ` | `singleLineText` | Type: singleLineText |  |
| **Aficion6raw**<br>`fldIuMLw0GYfSp2ji` | `singleLineText` | Type: singleLineText |  |
| **Aficion7raw**<br>`fldx79J05OQjTJku2` | `singleLineText` | Type: singleLineText |  |
| **Aficion8raw**<br>`fldmXruB6piPEMQ9u` | `singleLineText` | Type: singleLineText |  |
| **Aficion9raw**<br>`fldCP4v43fBtkID27` | `singleLineText` | Type: singleLineText |  |
| **Aficion10raw**<br>`fld6orcJdxz02HT18` | `singleLineText` | Type: singleLineText |  |
| **Aficion1**<br>`fldZZXonFmnakB4Km` | `singleLineText` | Type: singleLineText |  |
| **Aficion2**<br>`fldLQ9U53qnzBbRF3` | `singleLineText` | Type: singleLineText |  |
| **Idolo1**<br>`fldZEhhnJy48IBVhT` | `singleLineText` | Type: singleLineText |  |
| **Idolo2**<br>`fldUw24CZD3iHMiWM` | `singleLineText` | Type: singleLineText |  |
| **HrsSemOirM**<br>`fldGBjDawyqFglQ7S` | `number` | Numeric field |  |
| **HrsSemPractM**<br>`fldZsIWURW91mrP8a` | `number` | Numeric field |  |
| **Instrumento**<br>`fldmy1fFOWR2kjVV0` | `singleLineText` | Type: singleLineText |  |
| **EstiloMusical**<br>`fldNpukSfb6IH43vE` | `singleLineText` | Type: singleLineText |  |
| **Instagram**<br>`fldkvzD6fEfYhuhYt` | `number` | Numeric field |  |
| **WhatsApp**<br>`flduHVOCeCvH0zJvy` | `number` | Numeric field |  |
| **TikTok**<br>`fldhYIKOaBroz2qHi` | `number` | Numeric field |  |
| **Twitch**<br>`fld7rZ4OvggS8xx7m` | `number` | Numeric field |  |
| **JuegosOnLine**<br>`fldNwmddj6IzUc3tu` | `number` | Numeric field |  |
| **GrabarContenido**<br>`fldZV6JWuBQJa48nw` | `number` | Numeric field |  |
| **Youtube**<br>`fldKDAa5NfgqmzJ3B` | `number` | Numeric field |  |
| **SeguirInfluencer**<br>`fldm7QswCWpPahgS3` | `number` | Numeric field |  |
| **OtraActCelular**<br>`fldDdzXEuUrlk1ta0` | `singleLineText` | Type: singleLineText |  |
| **JuegoFavorito**<br>`fldC90E33cGCvHDYU` | `singleLineText` | Type: singleLineText |  |
| **TemaSeguirRaw**<br>`fldDfStFjGlX791d1` | `singleLineText` | Type: singleLineText |  |
| **TemaSeguir1**<br>`fld4DOnNrw2nmefhO` | `singleLineText` | Type: singleLineText |  |
| **TemaSeguir2**<br>`fldtKJKUpmyjDmLfL` | `singleLineText` | Type: singleLineText |  |
| **AtraccionCelular1**<br>`fld12awnZ65HuqG68` | `singleLineText` | Type: singleLineText |  |
| **AtraccionCelular2**<br>`fld5vbtgcwy8Dkhfw` | `singleLineText` | Type: singleLineText |  |
| **LigaSemanal**<br>`fldS1JsvRTSfkXrna` | `singleLineText` | Type: singleLineText |  |
| **LigaSemanalVeces**<br>`fldUBmAl6m7bP5KWB` | `number` | Numeric field |  |
| **SerProfesional**<br>`fldtm3qrqVEv1JNRj` | `singleLineText` | Type: singleLineText |  |
| **PosicionEnCancha**<br>`fldOmmdHGJnmfR9ga` | `singleLineText` | Type: singleLineText |  |
| **VecesPorSemanaAmigos**<br>`fldqb58XhklWGXCxx` | `number` | Numeric field |  |
| **HacenConAmigos**<br>`fldh1FLPGYgIhQOoR` | `singleLineText` | Type: singleLineText |  |
| **LeyendoOtro**<br>`fldvFVcIS8lOnVlRB` | `singleLineText` | Type: singleLineText |  |
| **LibroLeidoVariasVeces**<br>`fldJDfzH5c4xa6QjG` | `singleLineText` | Type: singleLineText |  |
| **LecturaActual**<br>`fld7aHhy85nwO54j1` | `singleLineText` | Type: singleLineText |  |
| **LibroQueMasGusto**<br>`fldrGEIK0ejWHbeEo` | `singleLineText` | Type: singleLineText |  |
| **AutorFavorito**<br>`fldrmS6uN35wtY7YG` | `singleLineText` | Type: singleLineText |  |
| **AutorFavoritoRaw**<br>`fldUYlz7YXbvuK8C4` | `singleLineText` | Type: singleLineText |  |
| **DeporteContacto**<br>`fldmMnYwDNcPvfUk5` | `singleLineText` | Type: singleLineText |  |
| **Iglesia**<br>`fldgkTHdOcjRoPnJj` | `singleLineText` | Type: singleLineText |  |
| **SerieFavoritaRaw**<br>`fldD0wEDMGsBxnsQv` | `singleLineText` | Type: singleLineText |  |
| **SerieFavorita1**<br>`fldiBSnaYnfq5t4E2` | `singleLineText` | Type: singleLineText |  |
| **SerieFavorita2**<br>`fldlGm62xlJTNuD7y` | `singleLineText` | Type: singleLineText |  |
| **ResumenIntereses**<br>`fldVTXSltgWIhMGrv` | `formula` | Calculated field | Formula: `IF(
  OR({fldZEhhnJy48IBVhT}!="",{fldUw24CZD3iHMi...` |
| **PerfilPersonal**<br>`fldejUCTriHwI33Up` | `formula` | Calculated field | Formula: `IF(
  AND({fldHbIYoqRvJmhilD}!="", {fldy3i0Il590n...` |
| **estudianteNivelActual**<br>`fldQYAEOAiLZdq5GQ` | `singleLineText` | Type: singleLineText |  |
| **estudianteLetra**<br>`fld0TgfT3iA7jOHiz` | `singleLineText` | Type: singleLineText |  |
| **estudianteCursoActual**<br>`fld6sx3Pub41wg0ix` | `formula` | Calculated field | Formula: `{fldQYAEOAiLZdq5GQ}&'-'&{fld0TgfT3iA7jOHiz}` |
| **estudianteNumeroLista**<br>`fld5rxWqmlujVUv17` | `number` | Numeric field |  |
| **Anno5B**<br>`fldI9Upe47NIOYKfv` | `formula` | Calculated field | Formula: `SWITCH({fldQYAEOAiLZdq5GQ},"1M",YEAR(TODAY())-4,"2...` |
| **Anno6B**<br>`fld9LDnjm9qwBWuzH` | `formula` | Calculated field | Formula: `SWITCH({fldQYAEOAiLZdq5GQ},"1M",YEAR(TODAY())-3,"2...` |
| **Anno7B**<br>`fldiPgglAwP3BcR58` | `formula` | Calculated field | Formula: `SWITCH({fldQYAEOAiLZdq5GQ},"1M",YEAR(TODAY())-2,"2...` |
| **Anno8B**<br>`fld74ShOFOxl8jBrZ` | `formula` | Calculated field | Formula: `SWITCH({fldQYAEOAiLZdq5GQ},"1M",YEAR(TODAY())-1,"2...` |
| **Curso-Alfabetico**<br>`fldR45P4Hlg9RkAi2` | `formula` | Calculated field | Formula: `{fld6sx3Pub41wg0ix}&"-"&{fldceUdfAqVAOEb5M}` |
| **Parametro_General**<br>`fldptneotRxaKbyhz` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **UmbralStopDiagnostico5B**<br>`fldwrUlbAOLVsx3Cb` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **UmbralStopDiagnostico6B**<br>`fldfgVs2cokduoJxM` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **UmbralStopDiagnostico7B**<br>`fldcIUk9crPOabo1K` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **UmbralStopDiagnostico8B**<br>`fldZqYHp1N8oYnabW` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **5B_Brecha_LE_DIAG**<br>`fldMRy55V7mbzL0Uy` | `count` | Type: count |  |
| **5B_Brecha_LE**<br>`fldPYv3EFTkfUWmJt` | `count` | Type: count |  |
| **5B_Brecha_LE_LOGRADA**<br>`fld12kMODxZFQ9GdE` | `count` | Type: count |  |
| **6B_Brecha_LE_DIAG**<br>`fldNGxQoAqO3buDTp` | `count` | Type: count |  |
| **6B_Brecha_LE**<br>`fldSylmvWWmFSukhQ` | `count` | Type: count |  |
| **6B_Brecha_LE_LOGRADA**<br>`fldS2M8CfXtYaIuvg` | `count` | Type: count |  |
| **7B_Brecha_LE_DIAG**<br>`fldb0iGWEOUfVmTer` | `count` | Type: count |  |
| **7B_Brecha_LE**<br>`fldg2O2UKXZyrZfZq` | `count` | Type: count |  |
| **7B_Brecha_LE_LOGRADA**<br>`fldnpXuBzS8pbY3px` | `count` | Type: count |  |
| **8B_Brecha_LE_DIAG**<br>`fldFIFC7fc3EBSDh5` | `count` | Type: count |  |
| **8B_Brecha_LE**<br>`flduZWjoHVJJkUdCE` | `count` | Type: count |  |
| **8B_Brecha_LE_LOGRADA**<br>`fld3epzRp9m2XgFya` | `count` | Type: count |  |
| **5B_Brecha_MA_DIAG**<br>`fld19Cvg7jmYkIFEm` | `count` | Type: count |  |
| **5B_Brecha_MA**<br>`fldOCL6aI4YcuYiWa` | `count` | Type: count |  |
| **5B_Brecha_MA_LOGRADA**<br>`fldfAScrOB5GP0WKq` | `count` | Type: count |  |
| **6B_Brecha_MA_DIAG**<br>`fldXWc4FdXs0LRBbt` | `count` | Type: count |  |
| **6B_Brecha_MA**<br>`fldjCfhi8BWUUPGbt` | `count` | Type: count |  |
| **6B_Brecha_MA_LOGRADA**<br>`fldOFkNY4runslBYT` | `count` | Type: count |  |
| **7B_Brecha_MA_DIAG**<br>`fldiljNjead3Fx7Fa` | `count` | Type: count |  |
| **7B_Brecha_MA**<br>`fldDvXhTpj2u08f9q` | `count` | Type: count |  |
| **7B_Brecha_MA_LOGRADA**<br>`fldk6Znej8AvOG0S0` | `count` | Type: count |  |
| **8B_Brecha_MA_DIAG**<br>`fld5TwJEunFJrVnCM` | `count` | Type: count |  |
| **8B_Brecha_MA**<br>`fldknGpn8ejuOhvK1` | `count` | Type: count |  |
| **8B_Brecha_MA_LOGRADA**<br>`fld8BcajQWHYQOUH9` | `count` | Type: count |  |
| **5B_Brecha_HG_DIAG**<br>`fldjc3LjSK6G0GX2G` | `count` | Type: count |  |
| **5B_Brecha_HG**<br>`fldwK62Pm8X5O3Z6L` | `count` | Type: count |  |
| **5B_Brecha_HG_LOGRADA**<br>`fld67VpdSF57Ixf2R` | `count` | Type: count |  |
| **6B_Brecha_HG_DIAG**<br>`fld6tHij93HERkO7Z` | `count` | Type: count |  |
| **6B_Brecha_HG**<br>`fldTz0E0o41LI7DNq` | `count` | Type: count |  |
| **6B_Brecha_HG_LOGRADA**<br>`fldTsY1xzrv5PHYxi` | `count` | Type: count |  |
| **7B_Brecha_HG_DIAG**<br>`fldxVuvVH1fWMqFx5` | `count` | Type: count |  |
| **7B_Brecha_HG**<br>`fldQT4NkSZRDRSWMo` | `count` | Type: count |  |
| **7B_Brecha_HG_LOGRADA**<br>`fldiOR0ka38MmPDjr` | `count` | Type: count |  |
| **8B_Brecha_HG_DIAG**<br>`fldlq8pPummmQZ1ay` | `count` | Type: count |  |
| **8B_Brecha_HG**<br>`fldErerAPwe1fFHTl` | `count` | Type: count |  |
| **8B_Brecha_HG_LOGRADA**<br>`flduSUlLwpwNZw2GD` | `count` | Type: count |  |
| **5B_Brecha_CS_DIAG**<br>`fldPjlSY0UWlVSQLG` | `count` | Type: count |  |
| **5B_Brecha_CS**<br>`fld9iecKKTCvHbgt2` | `count` | Type: count |  |
| **5B_Brecha_CS_LOGRADA**<br>`fldVPgr33fVzk5Q45` | `count` | Type: count |  |
| **6B_Brecha_CS_DIAG**<br>`fldQaqc2rFxkeB1Oj` | `count` | Type: count |  |
| **6B_Brecha_CS**<br>`fldxBmLOA254ip9O2` | `count` | Type: count |  |
| **6B_Brecha_CS_LOGRADA**<br>`fldpJjvhEGkSTq3cI` | `count` | Type: count |  |
| **7B_Brecha_CS_DIAG**<br>`fldLglqrmbJHkH1aH` | `count` | Type: count |  |
| **7B_Brecha_CS**<br>`fld89kwgSMY9fbyGM` | `count` | Type: count |  |
| **7B_Brecha_CS_LOGRADA**<br>`fldhZEeiHP6UVMtA9` | `count` | Type: count |  |
| **8B_Brecha_CS_DIAG**<br>`fld3v7kxDuNwR5cNk` | `count` | Type: count |  |
| **8B_Brecha_CS**<br>`fldbQcayKCIUAM5mE` | `count` | Type: count |  |
| **8B_Brecha_CS_LOGRADA**<br>`fld2tKXmuYneNYZ5x` | `count` | Type: count |  |
| **Brecha_LE_DIAG**<br>`fldJbBJwZwvzxzF6H` | `formula` | Calculated field | Formula: `{fldMRy55V7mbzL0Uy}+{fldNGxQoAqO3buDTp}+{fldb0iGWE...` |
| **Brecha_LE**<br>`fldFd6y5N2qdxi9t3` | `formula` | Calculated field | Formula: `{fldPYv3EFTkfUWmJt}+{fldSylmvWWmFSukhQ}+{fldg2O2UK...` |
| **Brecha_LE_LOGRADA**<br>`fldmCkNlAaW8d8Odj` | `formula` | Calculated field | Formula: `{fld12kMODxZFQ9GdE}+{fldS2M8CfXtYaIuvg}+{fldnpXuBz...` |
| **Brecha_LE_LOGRADA_pp**<br>`fldrmqHeUD6Bs7x3f` | `formula` | Calculated field | Formula: `IF(
  {fldJbBJwZwvzxzF6H}>0,
    {fldmCkNlAaW8d8...` |
| **Brecha_MA_DIAG**<br>`fldQNrCqmsMosIKJb` | `formula` | Calculated field | Formula: `{fld19Cvg7jmYkIFEm}+{fldXWc4FdXs0LRBbt}+{fldiljNje...` |
| **Brecha_MA**<br>`fldWnoH6pPqBtdxlJ` | `formula` | Calculated field | Formula: `{fldOCL6aI4YcuYiWa}+{fldjCfhi8BWUUPGbt}+{fldDvXhTp...` |
| **Brecha_MA_LOGRADA**<br>`fldTm7kYlTcRoDyNB` | `formula` | Calculated field | Formula: `{fldfAScrOB5GP0WKq}+{fldOFkNY4runslBYT}+{fldk6Znej...` |
| **Brecha_MA_LOGRADA_pp**<br>`fldS2ikFJ4oCt1HYK` | `formula` | Calculated field | Formula: `IF(
  {fldQNrCqmsMosIKJb}>0,
    {fldTm7kYlTcRoD...` |
| **Brecha_HG_DIAG**<br>`fldgWd7BwRlXwMR4g` | `formula` | Calculated field | Formula: `{fldjc3LjSK6G0GX2G}+{fld6tHij93HERkO7Z}+{fldxVuvVH...` |
| **Brecha_HG**<br>`fldnQhqqBHiPyTeLq` | `formula` | Calculated field | Formula: `{fldwK62Pm8X5O3Z6L}+{fldTz0E0o41LI7DNq}+{fldQT4NkS...` |
| **Brecha_HG_LOGRADA**<br>`fldYtgJJQ2AYHB7R3` | `formula` | Calculated field | Formula: `{fld67VpdSF57Ixf2R}+{fldTsY1xzrv5PHYxi}+{fldiOR0ka...` |
| **Brecha_HG_LOGRADA_pp**<br>`fldUbBAYjUnvGEBA7` | `formula` | Calculated field | Formula: `IF(
  {fldgWd7BwRlXwMR4g}>0,
    {fldYtgJJQ2AYHB...` |
| **Brecha_CS_DIAG**<br>`fldCLOMbVo3k5Y4nU` | `formula` | Calculated field | Formula: `{fldPjlSY0UWlVSQLG}+{fldQaqc2rFxkeB1Oj}+{fldLglqrm...` |
| **Brecha_CS**<br>`fldVBywZJ4j8MSgz5` | `formula` | Calculated field | Formula: `{fld9iecKKTCvHbgt2}+{fldxBmLOA254ip9O2}+{fld89kwgS...` |
| **Brecha_CS_LOGRADA**<br>`fldjoLvsGAO9BpzcO` | `formula` | Calculated field | Formula: `{fldVPgr33fVzk5Q45}+{fldpJjvhEGkSTq3cI}+{fldhZEeiH...` |
| **Brecha_CS_LOGRADA_pp**<br>`fldcEZ22FWSdlIKLj` | `formula` | Calculated field | Formula: `IF(
  {fldCLOMbVo3k5Y4nU}>0,
    {fldjoLvsGAO9Bp...` |
| **BRECHA_TOTAL_DIAG**<br>`fldxVmxCKSy3u3UA0` | `formula` | Calculated field | Formula: `{fldJbBJwZwvzxzF6H}+{fldQNrCqmsMosIKJb}+{fldgWd7Bw...` |
| **BRECHA_TOTAL**<br>`fld0Q9sNzZWAWZWEC` | `formula` | Calculated field | Formula: `{fldFd6y5N2qdxi9t3}+{fldWnoH6pPqBtdxlJ}+{fldnQhqqB...` |
| **BRECHA_TOTAL_LOGRADA**<br>`fld3SKpn5VlLKkc05` | `formula` | Calculated field | Formula: `{fldmCkNlAaW8d8Odj}+{fldTm7kYlTcRoDyNB}+{fldYtgJJQ...` |
| **BRECHA_TOTAL_LOGRADA_pp**<br>`fldBBz36uVGjEHPqo` | `formula` | Calculated field | Formula: `IF(
  {fldxVmxCKSy3u3UA0}>0,
    {fld3SKpn5VlLKk...` |
| **TareasActivas_BR**<br>`fldkJJKB74COhlAqw` | `count` | Type: count |  |
| **TareasActivas_DI**<br>`fldC2IwtD45lNnXXx` | `count` | Type: count |  |
| **TareasActivas_DE**<br>`fldrarE3DduCem7F2` | `count` | Type: count |  |
| **TareasActivas_Total**<br>`flduCllNFthDxylnA` | `formula` | Calculated field | Formula: `{fldkJJKB74COhlAqw}+
{fldC2IwtD45lNnXXx}+
{fldra...` |
| **BrechasPorEstudiante**<br>`fldFPdiaU1sxohkfr` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **UsuariosWeb**<br>`fldUjy81asC55nH29` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Mis_Tareas**<br>`fldRXoJxGP3N7XCBL` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiantes_Progreso**<br>`fld56UlwVBJlUMBtM` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes_Progreso 2**<br>`fldBQaopb99YTIiIl` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiantes_Progreso 2 copy**<br>`fldY4bteyajheVDVI` | `singleLineText` | Type: singleLineText |  |
| **NEE_DX_DEL**<br>`fldICbcZreyPo8sJJ` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **NEE_DCALC_MAT**<br>`fldgKZg6zdlgX238N` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **NEE_TDAH**<br>`fld1Mju64sBdnmoSw` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **NEE_TEA**<br>`fldTrZ2PodsBxPOZN` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **NEE_MOTR**<br>`fldaARdHn4haXJdYV` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **NEE_SENS_MOT**<br>`fldFNNG6IwSPZjAGH` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **Perfil_NEE**<br>`fldGnnyH6XTfNY9F0` | `formula` | Calculated field | Formula: `IF(AND(OR({fldICbcZreyPo8sJJ}="No",{fldICbcZreyPo8...` |
| **NEE_TEL**<br>`fldKvVbwY8CRDJLx0` | `singleSelect` | Single choice dropdown | `No`, `Leve`, `Moderado`, `Severo` |
| **estudianteNombreSocial**<br>`fldAu7p3nASH3VlMu` | `singleLineText` | Type: singleLineText |  |
| **NEE_RespaldoExpertoActividad**<br>`fld4Uw8zoFZE4gT0B` | `multilineText` | Multi-line text |  |

---

## 📋 15. Estudiantes_Progreso

*Table ID: `tblyHy7Vtw315073G`*
*Fields: 51*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **rec**<br>`fldGZKiaRm2GFmqvU` | `autoNumber` | Type: autoNumber |  |
| **FechaDatos**<br>`fldexkKZUCSGokS5q` | `createdTime` | Auto-generated creation time |  |
| **MesDatos**<br>`fldq99dLBsdEnNJog` | `formula` | Calculated field | Formula: `MONTH({fldexkKZUCSGokS5q})` |
| **MesDatosTxt**<br>`fldhKpfrSZez2tU4v` | `formula` | Calculated field | Formula: `SWITCH({fldq99dLBsdEnNJog},
  1, "Enero",
  2, "...` |
| **estudianteRut**<br>`fldXJLRqWAimNVv0q` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **estudianteRutInput**<br>`fldUmjuCwr9Pjfcm5` | `singleLineText` | Type: singleLineText |  |
| **estudianteNivelActual**<br>`fldSYb0DY0GMVxHbU` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteCursoActual**<br>`fld8s8pESTZOenCNB` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **5B_Brecha_LE**<br>`fldRY6pt3Bf2C3Yex` | `number` | Numeric field |  |
| **5B_Brecha_LE_LOGRADOS**<br>`fldmAYM1NR6By6T07` | `number` | Numeric field |  |
| **6B_Brecha_LE**<br>`fldUyWIkkEhsABWMU` | `number` | Numeric field |  |
| **6B_Brecha_LE_LOGRADOS**<br>`fldkQ0vwK5uxRNUvQ` | `number` | Numeric field |  |
| **7B_Brecha_LE**<br>`fldi2poJ8FUl96Ruu` | `number` | Numeric field |  |
| **7B_Brecha_LE_LOGRADOS**<br>`flddBGFbvyvt4pM3u` | `number` | Numeric field |  |
| **8B_Brecha_LE**<br>`fldwZxFd5DEw21P7I` | `number` | Numeric field |  |
| **8B_Brecha_LE_LOGRADOS**<br>`fldr8kqG30yLj6KkC` | `number` | Numeric field |  |
| **5B_Brecha_MA**<br>`fldQCmsZ6MTZc5Ure` | `number` | Numeric field |  |
| **5B_Brecha_MA_LOGRADOS**<br>`fldHZ1hg5pSLOHS2i` | `number` | Numeric field |  |
| **6B_Brecha_MA**<br>`fldlCQD7wjRHCWiGx` | `number` | Numeric field |  |
| **6B_Brecha_MA_LOGRADOS**<br>`flddJMlLmUo5mT4LN` | `number` | Numeric field |  |
| **7B_Brecha_MA**<br>`fldFvyDIN1XhIfREu` | `number` | Numeric field |  |
| **7B_Brecha_MA_LOGRADOS**<br>`fldCfHFdV8MKjhDaE` | `number` | Numeric field |  |
| **8B_Brecha_MA**<br>`fldmnhLcwWehwo7f5` | `number` | Numeric field |  |
| **8B_Brecha_MA_LOGRADOS**<br>`fldETZCQjS4ZQuwOo` | `number` | Numeric field |  |
| **5B_Brecha_HG**<br>`fldyKHoEKQSSwaBBP` | `number` | Numeric field |  |
| **5B_Brecha_HG_LOGRADOS**<br>`fld6zDjVvpRHcZtDK` | `number` | Numeric field |  |
| **6B_Brecha_HG**<br>`fldVzB0PMMWyqefiu` | `number` | Numeric field |  |
| **6B_Brecha_HG_LOGRADOS**<br>`fldGAUiBKUMAzxLkI` | `number` | Numeric field |  |
| **7B_Brecha_HG**<br>`fldSTF99gHMqzZyhs` | `number` | Numeric field |  |
| **7B_Brecha_HG_LOGRADOS**<br>`fldJqz2ArBhnojWla` | `number` | Numeric field |  |
| **8B_Brecha_HG**<br>`fldGrPNpde9OXMjop` | `number` | Numeric field |  |
| **8B_Brecha_HG_LOGRADOS**<br>`fldiJr909klYruTY1` | `number` | Numeric field |  |
| **5B_Brecha_CS**<br>`fldbiPyz8BxipiSY6` | `number` | Numeric field |  |
| **5B_Brecha_CS_LOGRADOS**<br>`fld9LMvcKBnBCHPep` | `number` | Numeric field |  |
| **6B_Brecha_CS**<br>`fldzBX7DYK0R0wLj6` | `number` | Numeric field |  |
| **6B_Brecha_CS_LOGRADOS**<br>`fld7fitm5NquWpU7i` | `number` | Numeric field |  |
| **7B_Brecha_CS**<br>`flda9VS5guTWXiabQ` | `number` | Numeric field |  |
| **7B_Brecha_CS_LOGRADOS**<br>`fldtLIiTca3jQ2ea1` | `number` | Numeric field |  |
| **8B_Brecha_CS**<br>`flddQNwn8kDHiTHRI` | `number` | Numeric field |  |
| **8B_Brecha_CS_LOGRADOS**<br>`fldaG3Y1Iz6DQVACT` | `number` | Numeric field |  |
| **Brecha_LE**<br>`fldHdHUUbKl0fpLY7` | `formula` | Calculated field | Formula: `{fldRY6pt3Bf2C3Yex}+{fldUyWIkkEhsABWMU}+{fldi2poJ8...` |
| **Brecha_LE_LOGRADOS**<br>`fldVCzaO1dpUltVTj` | `formula` | Calculated field | Formula: `{fldmAYM1NR6By6T07}+{fldkQ0vwK5uxRNUvQ}+{flddBGFbv...` |
| **Brecha_MA**<br>`fldYnZ3VNxlobk9QN` | `formula` | Calculated field | Formula: `{fldQCmsZ6MTZc5Ure}+{fldlCQD7wjRHCWiGx}+{fldFvyDIN...` |
| **Brecha_MA_LOGRADOS**<br>`fldF3KT76Ns6wVzkQ` | `formula` | Calculated field | Formula: `{fldHZ1hg5pSLOHS2i}+{flddJMlLmUo5mT4LN}+{fldCfHFdV...` |
| **Brecha_HG**<br>`fldpQSMfZpdCg0Qgu` | `formula` | Calculated field | Formula: `{fldyKHoEKQSSwaBBP}+{fldVzB0PMMWyqefiu}+{fldSTF99g...` |
| **Brecha_HG_LOGRADOS**<br>`fldZo2wiKfc6bgKvA` | `formula` | Calculated field | Formula: `{fld6zDjVvpRHcZtDK}+{fldGAUiBKUMAzxLkI}+{fldJqz2Ar...` |
| **Brecha_CS**<br>`fldXB9SO7MeVuZS49` | `formula` | Calculated field | Formula: `{fldbiPyz8BxipiSY6}+{fldzBX7DYK0R0wLj6}+{flda9VS5g...` |
| **Brecha_CS_LOGRADOS**<br>`fld2ijMomfMPj08rk` | `formula` | Calculated field | Formula: `{fld9LMvcKBnBCHPep}+{fld7fitm5NquWpU7i}+{fldtLIiTc...` |
| **BRECHA_TOTAL**<br>`fld2QKOCXHRnE6y9G` | `formula` | Calculated field | Formula: `{fldHdHUUbKl0fpLY7}+{fldYnZ3VNxlobk9QN}+{fldpQSMfZ...` |
| **BRECHA_TOTAL_LOGRADOS**<br>`fldu4KHXfVhUBhaGM` | `formula` | Calculated field | Formula: `{fldVCzaO1dpUltVTj}+{fldF3KT76Ns6wVzkQ}+{fldZo2wiK...` |
| **Version2204**<br>`fldmv5A6I51QZI7Wu` | `singleLineText` | Type: singleLineText |  |

---

## 📋 16. EvaluacionTiposInteligencia

*Table ID: `tblQVff2vdbB7pUfQ`*
*Fields: 68*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTestudiante**<br>`fldjVVWUd1bHfbXYv` | `singleLineText` | Type: singleLineText |  |
| **VersionFormJF201**<br>`fldzNvwSPWiuTJP4p` | `singleLineText` | Type: singleLineText |  |
| **LI**<br>`fldX05W0LJdMxMp7b` | `number` | Numeric field |  |
| **LM**<br>`fldpoI69o49K4iy1Y` | `number` | Numeric field |  |
| **ES**<br>`flddXIx5vipEKlar5` | `number` | Numeric field |  |
| **MU**<br>`fldDIRb7F4PiLHd2o` | `number` | Numeric field |  |
| **CK**<br>`fldqvxzH3090jLrLP` | `number` | Numeric field |  |
| **IA**<br>`fldULFyD159OkQg2J` | `number` | Numeric field |  |
| **IE**<br>`fldM38mmcr1to6C8b` | `number` | Numeric field |  |
| **NA**<br>`fldxZCZp4AnoudIts` | `number` | Numeric field |  |
| **Rtotal**<br>`fld9E0MK3BWmUxF88` | `formula` | Calculated field | Formula: `{fld2eaTP6fJIPrYuR}&","&{fldKxeJmW89GCEDnG}&","&{f...` |
| **TIPOINT_PRIMERO**<br>`fld2UfjMgcAbV5wtd` | `singleLineText` | Type: singleLineText |  |
| **TIPOINT_SEGUNDO**<br>`fldoyax2nNLLLMnA9` | `singleLineText` | Type: singleLineText |  |
| **DesvStandar**<br>`fldkkFzUUFwtYyKu5` | `number` | Numeric field |  |
| **R1**<br>`fld2eaTP6fJIPrYuR` | `singleLineText` | Type: singleLineText |  |
| **R2**<br>`fldKxeJmW89GCEDnG` | `singleLineText` | Type: singleLineText |  |
| **R3**<br>`fldw36Qk2SB9DUBcZ` | `singleLineText` | Type: singleLineText |  |
| **R4**<br>`fldBukFB7v324pMqx` | `singleLineText` | Type: singleLineText |  |
| **R5**<br>`fldtQ31pdIOBeO9PF` | `singleLineText` | Type: singleLineText |  |
| **R6**<br>`fld8ngRDLRT5tZWES` | `singleLineText` | Type: singleLineText |  |
| **R7**<br>`fld9kiLqTk4qKKXcS` | `singleLineText` | Type: singleLineText |  |
| **R8**<br>`fldTRmS0Vh4GwmVSj` | `singleLineText` | Type: singleLineText |  |
| **R9**<br>`fldMF0A1UmikRVXsJ` | `singleLineText` | Type: singleLineText |  |
| **R10**<br>`fldxOMTStTtHleB6V` | `singleLineText` | Type: singleLineText |  |
| **R11**<br>`fldFZJvsTUaf82287` | `singleLineText` | Type: singleLineText |  |
| **R12**<br>`fldSnNy8X3luxIYnc` | `singleLineText` | Type: singleLineText |  |
| **R13**<br>`fldTYiKzmcbOklHiZ` | `singleLineText` | Type: singleLineText |  |
| **R14**<br>`fld0TnvCFokLoYTWl` | `singleLineText` | Type: singleLineText |  |
| **R15**<br>`fldCLz1eLpHDMwRgD` | `singleLineText` | Type: singleLineText |  |
| **R16**<br>`fldZtdlsSDGEHcLYD` | `singleLineText` | Type: singleLineText |  |
| **R17**<br>`fldEdL8V2jMlfIifc` | `singleLineText` | Type: singleLineText |  |
| **R18**<br>`fldlOrPC8w3V1NWwu` | `singleLineText` | Type: singleLineText |  |
| **R19**<br>`fldXXk8zaveh8xaCe` | `singleLineText` | Type: singleLineText |  |
| **R20**<br>`fldWd4JNe4dHAIGHY` | `singleLineText` | Type: singleLineText |  |
| **R21**<br>`fldNrheSiXN8Tyrgp` | `singleLineText` | Type: singleLineText |  |
| **R22**<br>`fldt0wtHNENtyAlPa` | `singleLineText` | Type: singleLineText |  |
| **R23**<br>`fldU2DDVCvUYXq9Eh` | `singleLineText` | Type: singleLineText |  |
| **R24**<br>`fldtJRiHPKYRIShBM` | `singleLineText` | Type: singleLineText |  |
| **R25**<br>`fldllJAlueO1kvQl7` | `singleLineText` | Type: singleLineText |  |
| **R26**<br>`fld53VFTTHmjrtdpo` | `singleLineText` | Type: singleLineText |  |
| **R27**<br>`fldbZ82QTW1c9YjDe` | `singleLineText` | Type: singleLineText |  |
| **R28**<br>`fld1pwyMU0ctZ7cqb` | `singleLineText` | Type: singleLineText |  |
| **R29**<br>`fldPGsaJdVxW5u2MU` | `singleLineText` | Type: singleLineText |  |
| **R30**<br>`fldLgajDPT3NrAozr` | `singleLineText` | Type: singleLineText |  |
| **R31**<br>`fldj8ZXldK1AYymaY` | `singleLineText` | Type: singleLineText |  |
| **R32**<br>`flds7czdl90oBU1JY` | `singleLineText` | Type: singleLineText |  |
| **R33**<br>`fldBINKCQF3M1znw0` | `singleLineText` | Type: singleLineText |  |
| **R34**<br>`fldPCgAsa3zInCIIT` | `singleLineText` | Type: singleLineText |  |
| **R35**<br>`fld9cuhrqDn1LaggH` | `singleLineText` | Type: singleLineText |  |
| **R36**<br>`fldFmiwheRXljy7we` | `singleLineText` | Type: singleLineText |  |
| **R37**<br>`fldPOIVfPgqFri6RF` | `singleLineText` | Type: singleLineText |  |
| **R38**<br>`fldZGs0z71XugsOP1` | `singleLineText` | Type: singleLineText |  |
| **R39**<br>`fldugxM6h8QOBxRKV` | `singleLineText` | Type: singleLineText |  |
| **R40**<br>`fldNfMVPoBksPHp4A` | `singleLineText` | Type: singleLineText |  |
| **R41**<br>`fld8ZaLBFQVypN6XM` | `singleLineText` | Type: singleLineText |  |
| **R42**<br>`fld5CS7LXbf1wohyH` | `singleLineText` | Type: singleLineText |  |
| **R43**<br>`fldcq3LnmCasoaip0` | `singleLineText` | Type: singleLineText |  |
| **R44**<br>`fldSg8jjq1oMrB9At` | `singleLineText` | Type: singleLineText |  |
| **R45**<br>`fldrFgQB3u9BAxbiC` | `singleLineText` | Type: singleLineText |  |
| **R46**<br>`fldTB9Tcv6l8qLpJ0` | `singleLineText` | Type: singleLineText |  |
| **R47**<br>`fldPAV8GPezjTc7up` | `singleLineText` | Type: singleLineText |  |
| **R48**<br>`fldKUONv4Dh6pfsbD` | `singleLineText` | Type: singleLineText |  |
| **R49**<br>`fldaU9ncsgAA7kULW` | `singleLineText` | Type: singleLineText |  |
| **R50**<br>`fldvvK2Q6eUPF2GBv` | `singleLineText` | Type: singleLineText |  |
| **RUTraw**<br>`fld1Hn8Z9o25MaY6p` | `singleLineText` | Type: singleLineText |  |
| **FechaCreado**<br>`fldNN4UY5tS07oiZr` | `createdTime` | Auto-generated creation time |  |
| **FechaModificado**<br>`fldnTACxDEODkdnEJ` | `createdTime` | Auto-generated creation time |  |
| **DuracionTxt**<br>`fldAgpl4867I0sEuI` | `singleLineText` | Type: singleLineText |  |

---

## 📋 17. FactoresKPI0

*Table ID: `tbly4A1ydSFJ337nf`*
*Fields: 6*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTsostenedor**<br>`fldX2nJmHnKvzsR63` | `singleLineText` | Type: singleLineText |  |
| **FactorObsAula-Docentes**<br>`fldaRtp7tJOqIi3vG` | `number` | Numeric field |  |
| **Factor-TamanioColegio**<br>`fldmDJ6RqSkTpFIIj` | `number` | Numeric field |  |
| **Factor-DiasAtrasoFEEDB**<br>`fldvLBYsa1FVlnE3B` | `number` | Numeric field |  |
| **Factor-DesempenioGeneral**<br>`fldYER8cCvAu8MPgS` | `number` | Numeric field |  |
| **Factor-DesempenioCvSocioem**<br>`fldXLEB0PQdmgbBMx` | `number` | Numeric field |  |

---

## 📋 18. Imagenes

*Table ID: `tblBowkXcmyID4anO`*
*Fields: 5*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Serial**<br>`fldmXSHR5uQI4cXIN` | `autoNumber` | Type: autoNumber |  |
| **DescripcionImagen**<br>`fldikNcmLhaDQtvlG` | `singleLineText` | Type: singleLineText |  |
| **TamanoPixels**<br>`fldAfCUMv4DSJxoNM` | `singleLineText` | Type: singleLineText |  |
| **Imagen**<br>`fldeIdHHmMOvNWhu6` | `multipleAttachments` | Type: multipleAttachments |  |
| **ImagenUrl**<br>`fldYdTtUlwBGZLDcg` | `url` | URL link |  |

---

## 📋 19. InfoInexia

*Table ID: `tblqGRownMXGjwAFv`*
*Fields: 13*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Rec**<br>`fldTJV0TtiHx5vBws` | `autoNumber` | Type: autoNumber |  |
| **FechaCreacion**<br>`fldF2bnZQMFWcYEIY` | `createdTime` | Auto-generated creation time |  |
| **EmailRemitente**<br>`fldopwM7i0SEk69nI` | `email` | Email address |  |
| **NombreRemitente**<br>`fldGltTxDNm8F27ah` | `singleLineText` | Type: singleLineText |  |
| **SeleccionRemitente**<br>`fldFPfEEBujWQ4w6e` | `multipleSelects` | Multiple choice dropdown | `Información general del Ecosistema INEXIA`, `Información de AULAS`, `Información de APODERADOS`, `Información de ALONDRA`, `Información de Servicios de Consultoría` *(+2 more)* |
| **RemitenteEsCliente**<br>`fld4xQdyTu2IxjtkG` | `singleSelect` | Single choice dropdown | `Sí`, `Lo era en otro establecimiento`, `No` |
| **RemitenteSolicitud**<br>`fld184QcMgg2kLbAx` | `multilineText` | Multi-line text |  |
| **RemitenteColegio**<br>`fldGCKbz7HhhUVkx4` | `singleLineText` | Type: singleLineText |  |
| **RemitenteRegion**<br>`fld6MOQTd7lD4msPM` | `singleSelect` | Single choice dropdown | `Región de Arica y Parinacota`, `Región de Tarapacá`, `Región de Antofagasta`, `Región de Atacama`, `Región de Coquimbo` *(+11 more)* |
| **RemitenteComuna**<br>`fldF1AyaWbk7N7VK1` | `singleLineText` | Type: singleLineText |  |
| **ConsultaUrgencia**<br>`fldUDZHHWcDkxR47O` | `singleSelect` | Single choice dropdown | `Alta, lo más pronto posible`, `Media, dentro del día está bien`, `Baja, no requiere respuesta` |
| **RemitenteTelefono**<br>`fldEqYv6pMm5rQ874` | `singleLineText` | Type: singleLineText |  |
| **RemitentePreferenciaMedio**<br>`fldTegEbVHzWh8Cof` | `singleSelect` | Single choice dropdown | `Sólo email`, `Sólo WhatsApp`, `Cualquiera de los dos` |

---

## 📋 20. Intereses

*Table ID: `tblFrwXjSJIb6xROZ`*
*Fields: 58*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **estudianteRut**<br>`fld4tJHOlNXwOsfLJ` | `multilineText` | Multi-line text |  |
| **Aficion1raw**<br>`fldd7PlLQvjrHxUbj` | `singleLineText` | Type: singleLineText |  |
| **Aficion2raw**<br>`fldRxsHae02zXkKph` | `singleLineText` | Type: singleLineText |  |
| **Aficion3raw**<br>`fldvG9DmGUqxbC6Sq` | `singleLineText` | Type: singleLineText |  |
| **Aficion4raw**<br>`fldjP98OUd2UPAU3M` | `singleLineText` | Type: singleLineText |  |
| **Aficion5raw**<br>`fldLouJDpCkG3lI36` | `singleLineText` | Type: singleLineText |  |
| **Aficion6raw**<br>`fldRelXJNBycB3ozF` | `singleLineText` | Type: singleLineText |  |
| **Aficion7raw**<br>`fldGRIVdSJqgCnGKp` | `singleLineText` | Type: singleLineText |  |
| **Aficion8raw**<br>`fldvH0GOTkSMnqcpR` | `singleLineText` | Type: singleLineText |  |
| **Aficion9raw**<br>`fldLzDHhQabq3mZiu` | `singleLineText` | Type: singleLineText |  |
| **Aficion10raw**<br>`fldf80oW0s9XLlfhv` | `singleLineText` | Type: singleLineText |  |
| **Idolo1**<br>`fld8oQtAwtE5rfhxg` | `singleLineText` | Type: singleLineText |  |
| **Idolo2**<br>`fld3gBgPMyDfqqEc9` | `singleLineText` | Type: singleLineText |  |
| **AficionX**<br>`fldOXQSEBRER0KKUj` | `formula` | Calculated field | Formula: `IF({fldd7PlLQvjrHxUbj}!="", " !!! "&{fldd7PlLQvjrH...` |
| **Aficion1**<br>`fld8JwAAshX73fq0J` | `formula` | Calculated field | Formula: `MID(
  {fldOXQSEBRER0KKUj},
  FIND("!!!",{fldOXQ...` |
| **Aficion2**<br>`fldUAI6iQlXwkPdVq` | `formula` | Calculated field | Formula: `MID(
  {fldOXQSEBRER0KKUj},
  FIND("!!!",{fldOXQ...` |
| **HrsSemOirM**<br>`fldPlSPnjt0CZZcnf` | `number` | Numeric field |  |
| **HrsSemPractM**<br>`fld8ch87ERJY55box` | `number` | Numeric field |  |
| **Instrumento**<br>`fldviArSBRrZ3Xhbn` | `singleLineText` | Type: singleLineText |  |
| **EstiloMusical**<br>`fldW93w526GFqIpL1` | `singleLineText` | Type: singleLineText |  |
| **SubPerfilIntereses**<br>`fldZdQ7DQmjvCgU00` | `formula` | Calculated field | Formula: `IF(
  OR(({fld8JwAAshX73fq0J}="escuchar música"),...` |
| **Instagram**<br>`fldtf8Pj2zPV08DeQ` | `number` | Numeric field |  |
| **WhatsApp**<br>`fldDru0P1x5EJd5LV` | `number` | Numeric field |  |
| **TikTok**<br>`fldqIhW1Xw1liGMXF` | `number` | Numeric field |  |
| **Twitch**<br>`fldgbyg1ibQPRbTnJ` | `number` | Numeric field |  |
| **JuegosOnLine**<br>`fldWgVpq61iwDQpJR` | `number` | Numeric field |  |
| **GrabarContenido**<br>`fld8FFV9hwqGTIuDT` | `number` | Numeric field |  |
| **Youtube**<br>`fldTn9miAaQn5d5jY` | `number` | Numeric field |  |
| **SeguirInfluencer**<br>`fldvRpEJpRZMTVC8q` | `number` | Numeric field |  |
| **AtraccionMax**<br>`fldDjz6LdqZftfnSB` | `formula` | Calculated field | Formula: `MAX(
  {fldtf8Pj2zPV08DeQ}, 
  {fldDru0P1x5EJd5L...` |
| **AtraccionCelular1**<br>`fldaMJIAM1FEd42mv` | `formula` | Calculated field | Formula: `IF({fldDjz6LdqZftfnSB}={fldtf8Pj2zPV08DeQ}, "Insta...` |
| **OtraActCelular**<br>`fldMX89RhP1i3FPqn` | `singleLineText` | Type: singleLineText |  |
| **JuegoFavoritoRaw**<br>`fldyWsQUWxOKBvgr8` | `singleLineText` | Type: singleLineText |  |
| **JuegoFavorito1**<br>`fldLTzQgQ7gzelZeh` | `singleLineText` | Type: singleLineText |  |
| **JuegoFavorito2**<br>`fld3aJW2WX9YRa7mw` | `singleLineText` | Type: singleLineText |  |
| **TemaSeguirRaw**<br>`fldMZrFS6BVUQNnto` | `singleLineText` | Type: singleLineText |  |
| **TemaSeguir1**<br>`flddnnz0erCk5SBxb` | `singleLineText` | Type: singleLineText |  |
| **TemaSeguir2**<br>`fldCuiW7ch8gm07v8` | `singleLineText` | Type: singleLineText |  |
| **InfluencerPreferido**<br>`fld1NihQPu24oxaSq` | `singleLineText` | Type: singleLineText |  |
| **AtraccionCelular2**<br>`fldefKFtZr85mYDvT` | `singleLineText` | Type: singleLineText |  |
| **LigaSemanal**<br>`fld1LiEIEOsc3BNDx` | `singleLineText` | Type: singleLineText |  |
| **LigaSemanalVeces**<br>`fld3lVMyThH8yJ6cY` | `number` | Numeric field |  |
| **SerProfesional**<br>`fldC6CCEdQesKn97G` | `singleLineText` | Type: singleLineText |  |
| **PosicionEnCancha**<br>`fldX6VpUtEXjYvvwx` | `singleLineText` | Type: singleLineText |  |
| **VecesPorSemanaAmigos**<br>`fldzVEka4fVTpBYNU` | `number` | Numeric field |  |
| **HacenConAmigos**<br>`fldqLeX2tTQF0uaEe` | `singleLineText` | Type: singleLineText |  |
| **LeyendoOtro**<br>`fldEpuoVF3VL6zH7Y` | `singleLineText` | Type: singleLineText |  |
| **LibroLeidoVariasVeces**<br>`fldSnOLUS7EuTKcz3` | `singleLineText` | Type: singleLineText |  |
| **LecturaActual**<br>`fldgUgtLV0XtxJqzo` | `singleLineText` | Type: singleLineText |  |
| **LibroQueMasGusto**<br>`fldAqdUXN9TTqPAUL` | `singleLineText` | Type: singleLineText |  |
| **AutorFavorito**<br>`fldA6riHAYFtcCte3` | `singleLineText` | Type: singleLineText |  |
| **AutorFavoritoRaw**<br>`fld3IULkLSLsdouSr` | `singleLineText` | Type: singleLineText |  |
| **DeporteContacto**<br>`fldvwWaJqIMMeTgAs` | `singleLineText` | Type: singleLineText |  |
| **Iglesia**<br>`fldp4sTqB7TO7tJZG` | `singleLineText` | Type: singleLineText |  |
| **SerieFavoritaRaw**<br>`fldMK5QQzB2yg1O6S` | `singleLineText` | Type: singleLineText |  |
| **SerieFavorita1**<br>`fldrlrznLiPnO7qUp` | `singleLineText` | Type: singleLineText |  |
| **SerieFavorita2**<br>`flduqVifkgjQw8ZnV` | `singleLineText` | Type: singleLineText |  |
| **estudianteFechaEncuestaIntereses**<br>`fldlhiAnjPxQpRCQJ` | `createdTime` | Auto-generated creation time |  |

---

## 📋 21. LogAccesos

*Table ID: `tblzy5w53DpT6AXq1`*
*Fields: 2*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTusuario**<br>`fldAikhObC7mTJ39w` | `singleLineText` | Type: singleLineText |  |
| **loginFecha**<br>`fldjngl2CEZOoz0rx` | `dateTime` | Date and time |  |

---

## 📋 22. Mis_Tareas

*Table ID: `tblbZucEDW4BUg12x`*
*Fields: 35*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **tareaCodigo**<br>`fldhh98o3Hx5NBj0i` | `autoNumber` | Type: autoNumber |  |
| **estudianteRUT**<br>`fldQviQUN9abQ6s8L` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **estudianteRUT2**<br>`fldkJoILCM0of1U3u` | `singleLineText` | Type: singleLineText |  |
| **tareaTipo**<br>`fldPJ6dtT8Jy7kU4B` | `singleLineText` | Type: singleLineText |  |
| **tareaGuardada**<br>`fld6unsmNfljf3auk` | `number` | Numeric field |  |
| **tareaFechaGuardada**<br>`fldNgiA2UB8VmHRmO` | `dateTime` | Date and time |  |
| **colegioNombre**<br>`fldWhC6mHzRrL1xZp` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioSigla**<br>`fldrE9VNX3XIM1Pu8` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaNacimiento**<br>`fldM1UVDGMV46M65t` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteNombre**<br>`fldtP9tUEPfSCwTfa` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudiantePaterno**<br>`fldWUZCnslnL9CLjJ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteNombreCompleto**<br>`fldxZa9bnF4QkdbON` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TareaActNumero**<br>`fldeG80f30NtVYJHG` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **OA**<br>`fldTQxfk4rhPGxkKw` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OA2**<br>`fldCGXpZq4DN4sO3h` | `singleLineText` | Type: singleLineText |  |
| **OAdescripcion**<br>`flds0clNiuJVJD1fe` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAmateria**<br>`fldLuA5kUAo7C7d58` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **OAeje**<br>`fld4cvZ5bHrLIUsHB` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **tareaFechaAsignacion**<br>`fldSzEm29fsWCotDl` | `createdTime` | Auto-generated creation time |  |
| **tareaFechaAsignacionSinH**<br>`fld58lIfHg7L1vW2u` | `formula` | Calculated field | Formula: `T(DATETIME_FORMAT({fldSzEm29fsWCotDl}, 'DD/MM/YYYY...` |
| **DemoraEjecucion**<br>`fldNxkA4J3Uxmcv3E` | `formula` | Calculated field | Formula: `IF(
  {fldZN7ZNC61bHCu8R}=2,
  WORKDAY_DIFF(
  ...` |
| **tareaPlazoDias**<br>`fldI0pjasoXrAm1me` | `number` | Numeric field |  |
| **tareaDescripcion**<br>`fldInmwGG4Bne6203` | `singleLineText` | Type: singleLineText |  |
| **tareaLinkRaw**<br>`fldELRYRTx11pnkBF` | `url` | URL link |  |
| **tareaLink**<br>`fldxj9DuSCDdIeDNw` | `formula` | Calculated field | Formula: `{fldELRYRTx11pnkBF}&"?rut="&{fldkJoILCM0of1U3u}&"&...` |
| **tareaConNota**<br>`fldkZ1cBl7Ua9C7ul` | `checkbox` | True/False checkbox |  |
| **tareaObligatoria**<br>`fldHF27ypRbc8q96m` | `checkbox` | True/False checkbox |  |
| **tareaRecursos**<br>`flddO6g5wOWT3uz5X` | `singleLineText` | Type: singleLineText |  |
| **tareaGrupal**<br>`fldSD6A6DATMiyAWn` | `checkbox` | True/False checkbox |  |
| **tareaLugar**<br>`fldxt4rPuY4Say2PS` | `singleLineText` | Type: singleLineText |  |
| **tareaEjecutada**<br>`fldZN7ZNC61bHCu8R` | `number` | Numeric field |  |
| **tareaFechaEjecucion**<br>`fldXibCSVyfkkxMJx` | `dateTime` | Date and time |  |
| **tareaResultado**<br>`fld6KjQuXASfWoQAz` | `singleLineText` | Type: singleLineText |  |
| **tareaEstado**<br>`fldC3AeItVPRgZ9qE` | `number` | Numeric field |  |
| **Guardado**<br>`flderU733tsfMKe7g` | `checkbox` | True/False checkbox |  |

---

## 📋 23. miniExtensions

*Table ID: `tbl57ZETu884T1nul`*
*Fields: 3*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Primary field**<br>`fldBBk6qEVksL6wxw` | `singleLineText` | Type: singleLineText |  |
| **RutaEstudianteHistorica**<br>`fldAlD8nau5geL0BG` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Docentes**<br>`fldI9aIuej46P6AQQ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 24. NEE

*Table ID: `tbldQgQrLHrHUb5Kj`*
*Fields: 2*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **NEE_codigo**<br>`fldYswLUcdKXcTFo0` | `singleLineText` | Type: singleLineText |  |
| **NEE_nombre**<br>`fldmKSlkV9dELG2Q1` | `multilineText` | Multi-line text |  |

---

## 📋 25. ObservacionesAula

*Table ID: `tblkCt3OoYP9VxSaQ`*
*Fields: 302*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **NumeroOA**<br>`fld0UTjgTSsrHI2dX` | `autoNumber` | Type: autoNumber |  |
| **ObsAulaTipo**<br>`fldP6vl5BwJWY6HKo` | `singleLineText` | Type: singleLineText |  |
| **FechaObsAula**<br>`fldHAZn5seSh1HeNs` | `dateTime` | Date and time |  |
| **FechaCreacionRegistro**<br>`fldpsfTaDqUk09Y3G` | `createdTime` | Auto-generated creation time |  |
| **AntiguedadObsAula**<br>`fldjjIQ7NLsggLpnd` | `formula` | Calculated field | Formula: `DATETIME_DIFF({fldHAZn5seSh1HeNs},'01/01/2000','d'...` |
| **MacroVersionA010**<br>`fldfSR3QyTzGGa7wN` | `singleLineText` | Type: singleLineText |  |
| **VersionFormA010**<br>`fldbHGGI9VxvellEm` | `singleLineText` | Type: singleLineText |  |
| **VersionTabla**<br>`fldWdYX4dVartpfvo` | `singleLineText` | Type: singleLineText |  |
| **ColegioSigla**<br>`fldHZIUFDgNYVW8fe` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **LapsoEntrevistaObs**<br>`fldRu6G6KiSWHf59o` | `formula` | Calculated field | Formula: `IF({fldnAO4XWFuw045JK} != "",
DATETIME_DIFF({fldn...` |
| **flagDePaso**<br>`fldXi7A6WbQxTAda5` | `number` | Numeric field |  |
| **ColegioSiglaTag**<br>`fld962azjrzb6H5Mf` | `formula` | Calculated field | Formula: `{fldHZIUFDgNYVW8fe}` |
| **Sostenedor**<br>`fldRiDkf0WR2hFP2P` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **superiorFEEDBemail**<br>`fldxYAH2bgsfHap2B` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ObsAulaTipoTag**<br>`fldo8q0kw4FFsEuzM` | `singleSelect` | Single choice dropdown | `Clase completa`, `Inicio`, `Cierre`, `Parte del Desarrollo` |
| **EmitePDF1**<br>`fldfq1Nhy5fOlsVKz` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioEnObservacion**<br>`fld8wGYZq13B6p7Is` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaStr**<br>`fldKPKvwvitbw2Lee` | `formula` | Calculated field | Formula: `DATETIME_FORMAT({fldHAZn5seSh1HeNs}, "DD/MM/YYYY")...` |
| **Anno**<br>`fldFcckrk8vp8JaxR` | `formula` | Calculated field | Formula: `YEAR({fldHAZn5seSh1HeNs})` |
| **Mes**<br>`fldig9voFXRdxg2pm` | `formula` | Calculated field | Formula: `MONTH({fldHAZn5seSh1HeNs})` |
| **TrimSem**<br>`fldhjl7pTei0hfIB9` | `number` | Numeric field |  |
| **HorarioClase**<br>`fldYpzlc1sG57j4nA` | `singleSelect` | Single choice dropdown | `A continuación de recreo sin turno de patio solidario`, `Primera hora de la mañana después de 15 min jefatura`, `A continuación de recreo con turno de patio solidario`, `A continuación de otra hora de clases`, `Primera hora de la mañana  (High)` *(+1 more)* |
| **FEEDB_html_MiniE**<br>`fldGhvIE6NH2gYJD2` | `formula` | Calculated field | Formula: `CONCATENATE(
"<script>\\r\ndocument.addEventListe...` |
| **ReintentosAlarmaFEEDB**<br>`fld6zOC2GrOebFsSU` | `number` | Numeric field |  |
| **DiasDesdeFechaObsAula**<br>`fldEqzJxw5I5f52dG` | `formula` | Calculated field | Formula: `DATETIME_DIFF(
  TODAY(),{fldHAZn5seSh1HeNs},'day...` |
| **FechaUltimaAlarmaEntrevista**<br>`fldsgUcBdRrYMuqid` | `date` | Date |  |
| **DiasDesdeUltimaAlarma**<br>`fldfveK3TlHIUaFAo` | `formula` | Calculated field | Formula: `IF({fldsgUcBdRrYMuqid}!="",
  DATETIME_DIFF(TODAY...` |
| **Trimestre_tag**<br>`fldcU4TlpZlkQjkrk` | `singleSelect` | Single choice dropdown | `1`, `2`, `3` |
| **CursoTxt**<br>`fldZtWcy2Cat4ZlFq` | `singleLineText` | Type: singleLineText |  |
| **Curso**<br>`fldalosVo0QuAy0DI` | `singleSelect` | Single choice dropdown | `__Play`, `__PreKinder A`, `__PreKinder B`, `__PreKinder C`, `__PreKinder D` *(+50 more)* |
| **CursoNivel**<br>`fld6LtLSLgEUXseTy` | `formula` | Calculated field | Formula: `IF(FIND("Play",{fldalosVo0QuAy0DI})>0,
  "Play",...` |
| **CursoNiveltag**<br>`fldj6YetDDO5Puc05` | `singleSelect` | Single choice dropdown | `PreKinder`, `Kinder`, `2° Básico`, `3° Básico`, `4° Básico` *(+11 more)* |
| **Ciclo**<br>`fldbgAP5pgjJD9rRI` | `singleLineText` | Type: singleLineText |  |
| **CicloTag**<br>`flddjmokbB7roq614` | `singleSelect` | Single choice dropdown | `Junior`, `Infant`, `Middle`, `High`, `Primer Ciclo Básico` |
| **Asignatura**<br>`fldRDQcAdcSJskG7i` | `singleLineText` | Type: singleLineText |  |
| **Departamento**<br>`fldhL3dd2NvzBawUj` | `formula` | Calculated field | Formula: `IF(
  OR(
    {fldRDQcAdcSJskG7i} = "Identidad y...` |
| **Departamento_tag**<br>`fldglEkvXYpCA5sF5` | `singleSelect` | Single choice dropdown | `Lenguaje`, `Matemática`, `Inglés`, `Ciencias`, `Historia, Geografía y Formación ciudadana` *(+4 more)* |
| **DocenteObservado**<br>`fldIxVua81KtYGjVh` | `singleLineText` | Type: singleLineText |  |
| **RUTDocente**<br>`fld0hiuvzwiGh2uNM` | `singleLineText` | Type: singleLineText |  |
| **RUTDocenteObservadoLookUp**<br>`fld7cDjPeEvLUdvwb` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **DocenteObservado_tag**<br>`fldMJQHXIPD8qHwSR` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **NombreCompletoDocente**<br>`fldsFH72q7tzftGDY` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **NombresPilaDocente**<br>`flddBHzB1eYiS60lj` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **DesempennoGeneral**<br>`fldA2C25xXLvVFMO4` | `formula` | Calculated field | Formula: `ROUND(
  (
    {fldXNGss6gvusit5z}+
    {fldPgy...` |
| **DesempennoGeneralCalif**<br>`fldfXoNFBe231o0gQ` | `formula` | Calculated field | Formula: `IF({fldA2C25xXLvVFMO4}=4,"🏆 Sobresaliente",
   IF...` |
| **Evaluador**<br>`fldEyJAsWwMs3IJ8y` | `singleLineText` | Type: singleLineText |  |
| **EvaluadorTag**<br>`fldXerv4MNGxbUir0` | `singleSelect` | Single choice dropdown | `Paula Neill`, `González Arancibia, Raúl`, `Vargas , Luis Valentín`, `Lodi , Claudia`, `Dapelo , Rossana` *(+17 more)* |
| **EmailEvaluador**<br>`fldXnWSfH3yVaetl9` | `singleLineText` | Type: singleLineText |  |
| **INEXIA_A010_Sugerencia**<br>`fldyKAwbHjISGqBXw` | `multilineText` | Multi-line text |  |
| **PromptIAguionEntrevista**<br>`fld1WUEA6AwdhntCr` | `formula` | Calculated field | Formula: `"Escala de evaluación: Sobresaliente/Bueno/Básico/...` |
| **GuionEntr-PresFort**<br>`flduPvuT0wYL08mEY` | `multilineText` | Multi-line text |  |
| **GuionEntr-Deb**<br>`fldGdwGEDerxv82DJ` | `multilineText` | Multi-line text |  |
| **GuionEntr-Ppta**<br>`fldQyi4dwmpHvHGok` | `multilineText` | Multi-line text |  |
| **GuionEntr-Cierre**<br>`fldrt3pA0Iin0lK6b` | `multilineText` | Multi-line text |  |
| **AspectoClaveEntrevista**<br>`fldXXLsM35kp63ZPP` | `multilineText` | Multi-line text |  |
| **ConsejoTactico**<br>`fldbnzBm5d8ld3Wki` | `multilineText` | Multi-line text |  |
| **ModeloGuion**<br>`fldiAnPE0dOV5CPqv` | `singleLineText` | Type: singleLineText |  |
| **FechaGuion**<br>`fld0idWch0E1OEvrI` | `singleLineText` | Type: singleLineText |  |
| **Version9005**<br>`fldxAKcmXQ0i68mAU` | `singleLineText` | Type: singleLineText |  |
| **CuantosInsuficientes**<br>`fldAi0RcBNfR82Qu2` | `formula` | Calculated field | Formula: `IF({fldXNGss6gvusit5z}=1,1,0)+
IF({fldPgyoWmGQWzm...` |
| **CuantosBasicos**<br>`fldvH1dWtsF3pqz9C` | `formula` | Calculated field | Formula: `IF({fldXNGss6gvusit5z}=2,1,0)+
IF({fldPgyoWmGQWzm...` |
| **CuantosBuenos**<br>`fldN9tqpO0dmZ4gP3` | `formula` | Calculated field | Formula: `IF({fldXNGss6gvusit5z}=3,1,0)+
IF({fldPgyoWmGQWzm...` |
| **CuantosSobresalientes**<br>`fldlArjr4YWfrTWqZ` | `formula` | Calculated field | Formula: `IF({fldXNGss6gvusit5z}=4,1,0)+
IF({fldPgyoWmGQWzm...` |
| **DuracionClase**<br>`fldcsJcKyi4BG9z75` | `number` | Numeric field |  |
| **DuracionObservacion**<br>`fldSrmx9ZASPTdc2s` | `number` | Numeric field |  |
| **CalificacionTiempoTrabajoTxt**<br>`fldGa9IX9YyAWrWni` | `number` | Numeric field |  |
| **CalificacionTiempoTrabajo**<br>`fldsZog0vm405Vlrw` | `number` | Numeric field |  |
| **PROMEDIO_CVSOCIOEM**<br>`fldZY9VpBpFBNjttw` | `formula` | Calculated field | Formula: `IF(
  ({fld2NI9dWEeyQh9ic}+
   {fldQtaLOxZrVgyrE...` |
| **PROMEDIO_CVSOCIOEMtxt**<br>`fldnz4kqmiau7ytIk` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldZY9VpBpFBNjttw},0),
  4, "Sobres...` |
| **ValorInclusion**<br>`fld2NI9dWEeyQh9ic` | `formula` | Calculated field | Formula: `IF(
  ({fldJMMr23Vyrb03Ee}+
  {flduRfYIZ9sECZMu5...` |
| **ValorInclusionTxt2**<br>`fldNLqHjyvJAWSbm3` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fld2NI9dWEeyQh9ic},0),
  4, "Sobres...` |
| **ValorAutonomia**<br>`fldQtaLOxZrVgyrEq` | `formula` | Calculated field | Formula: `IF(
  (
    {fldiTxBBcNJOCS1jd}+
    {fldsfGYPE...` |
| **ValorAutonomiaTxt**<br>`fldW8bLbTxOP8mC6x` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldQtaLOxZrVgyrEq},0),
  4, "Sobres...` |
| **ValorDesarrSocioem**<br>`fldgW7VWC6P89kPfw` | `formula` | Calculated field | Formula: `IF(
  (
    {fldFTua08ZQP93IPt}+
    {fld8Elpa9...` |
| **ValorDesarrSocioemTxt**<br>`fldlzLMZaPbu6tG3c` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldgW7VWC6P89kPfw},0),
  4, "Sobres...` |
| **ValorConvivenciaAutoridad**<br>`fldJkeHP5idQX1qw7` | `formula` | Calculated field | Formula: `IF(
  (
    {fldPHR3Or1cbtHcdy}+
    {fldXNGss6...` |
| **ValorConvivenciaAutoridadTxt**<br>`fldwfNXQt3DL2n0iq` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldJkeHP5idQX1qw7},0),
  4, "Sobres...` |
| **PROMEDIO_ENSEÑANZA**<br>`fldWEewnZoZMmhmGD` | `formula` | Calculated field | Formula: `IF(
  ({fldBXxajODHbNmrKN}+
   {fldgFOklVKTjkrCM...` |
| **PROMEDIO_ENSEÑANZAtxt**<br>`fldkxmE3F62GOK135` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldWEewnZoZMmhmGD},0),
  4, "Sobres...` |
| **ValorPlanificacion**<br>`fldBXxajODHbNmrKN` | `formula` | Calculated field | Formula: `IF(
  (
    {fldXt2J3xwtepv1Bu} +
    {fldynAV9...` |
| **ValorPlanificacionTxt**<br>`fldlhpGKle8uHU81N` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldBXxajODHbNmrKN},0),
  4, "Sobres...` |
| **ValorEstrategiasPedag**<br>`fldgFOklVKTjkrCM6` | `formula` | Calculated field | Formula: `IF(
  (
    {fld8Elpa9nqkSakOf}+
    {fldndGuiB...` |
| **ValorEstrategiasPedagTxt**<br>`fldk7fzBUnEdYtb5H` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldgFOklVKTjkrCM6},0),
  4, "Sobres...` |
| **ValorGestionAulaYCv**<br>`fldu1lLaja8nsNmC5` | `formula` | Calculated field | Formula: `IF(
  (
    {fldPHR3Or1cbtHcdy}+
    {fldXNGss6...` |
| **ValorGestionAulaYCvTxt**<br>`fldXWMC4ivkN3w4G7` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldu1lLaja8nsNmC5},0),
  4, "Sobres...` |
| **ValorRelacEstud**<br>`fldGxBXqxN3TWd6HB` | `formula` | Calculated field | Formula: `IF(
  (
    {fldFTua08ZQP93IPt}+
    {fldOlChoO...` |
| **ValorRelacEstudTxt**<br>`fldR6xOesYvy1hurg` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldGxBXqxN3TWd6HB},0),
  4, "Sobres...` |
| **ValorEvaluacYRetro**<br>`fldT0ifPKggJzvb9Z` | `formula` | Calculated field | Formula: `IF(
  (
    {fldmJr8y69zwx99jp}+
    {fldb42vK7...` |
| **ValorEvaluacYRetroTxt**<br>`fldZkpyaxAtwr3fmU` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldT0ifPKggJzvb9Z},0),
  4, "Sobres...` |
| **ValorIngles**<br>`fldwmcLa98rpWGToX` | `formula` | Calculated field | Formula: `IF(
  (
    {fld6pfgM5dj5zQS8V}+
    {fldHbliR1...` |
| **ValorInglesTxt**<br>`fldQKXTnDyOn0hq55` | `formula` | Calculated field | Formula: `SWITCH(ROUND({fldwmcLa98rpWGToX},0),
  4, "Sobres...` |
| **ValorPrebasica**<br>`flduPtbtnrY4yD3OS` | `formula` | Calculated field | Formula: `IF(
  (
    {fldP9hv7Z4t3xosWA}+
    {fldk4Rlep...` |
| **ValorPrebasicaTxt**<br>`fldx7A9C6NA3kYXL7` | `formula` | Calculated field | Formula: `SWITCH(ROUND({flduPtbtnrY4yD3OS},0),
  4, "Sobres...` |
| **INI_LlegaPuntual**<br>`fldPHR3Or1cbtHcdy` | `number` | Numeric field |  |
| **INI_LlegaPuntualTxt**<br>`fldyb3z6nZAg76NiW` | `singleSelect` | Single choice dropdown | `Llega apenas toca`, `Llega levemente tarde`, `Está en la puerta antes del toque de timbre`, `Evaluador(a) no observa esta parte de la clase` |
| **INI_ReaccionRespeto**<br>`fldXNGss6gvusit5z` | `number` | Numeric field |  |
| **INI_ReaccionRespetoTxt**<br>`fldTSTmosTr9lrJQS` | `singleSelect` | Single choice dropdown | `Aceptable`, `Bueno`, `Básico`, `Insatisfactorio`, `Sobresaliente` *(+5 more)* |
| **INI_LograAmbiente**<br>`fldPgyoWmGQWzmfuH` | `number` | Numeric field |  |
| **INI_LograAmbienteTxt**<br>`fldPGe2cw5dxO0FsD` | `singleSelect` | Single choice dropdown | `Bueno`, `Excelente`, `Sobresaliente`, `Básico`, `Logra un buen ambiente de trabajo` *(+3 more)* |
| **INI_ComunicNoVerbal**<br>`fldaqqKLthUwlhs5n` | `number` | Numeric field |  |
| **INI_ComunicNoVerbalTxt**<br>`fldPFyM0TAgcsJQTy` | `singleSelect` | Single choice dropdown | `Aceptable`, `Sobresaliente`, `Excelente`, `Bueno`, `Insatisfactorio` *(+5 more)* |
| **INI_ClaridadObjetivos**<br>`fldjgXXOCwn5cWDns` | `number` | Numeric field |  |
| **INI_ClaridadObjetivosTxt**<br>`fldiWY00WnPMmGfMV` | `singleSelect` | Single choice dropdown | `Aceptable`, `Sobresaliente`, `Excelente`, `Bueno`, `Básico` *(+4 more)* |
| **INI_ConectaContAnteriores**<br>`fldndGuiBf3WCAbTV` | `number` | Numeric field |  |
| **INI_ConectaContAnterioresTxt**<br>`fldPrCKGNe6SwsGUH` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Excelente`, `Aceptable`, `Bueno`, `Básico` *(+4 more)* |
| **INI_ActivaMotivacion**<br>`fld8Elpa9nqkSakOf` | `number` | Numeric field |  |
| **INI_ActivaMotivacionTxt**<br>`fldCDep0WjfEgiutH` | `singleSelect` | Single choice dropdown | `Excelente`, `Bueno`, `Aceptable`, `Deficiente`, `Sobresaliente` *(+6 more)* |
| **INI_MaterialesListos**<br>`fldBrQYhNtGLYv9Rs` | `number` | Numeric field |  |
| **INI_MaterialesListosTxt**<br>`fldXMPKd2Bag2Hzge` | `singleSelect` | Single choice dropdown | `Deficiente`, `Aceptable`, `Bueno`, `Insatisfactorio`, `Sobresaliente` *(+6 more)* |
| **INI_EsbleceLimitesClaros**<br>`fldLCB5Zf12rH7v4s` | `number` | Numeric field |  |
| **INI_EsbleceLimitesClarosTxt**<br>`fldhQfCeBj0P4FVBQ` | `singleSelect` | Single choice dropdown | `Deficiente`, `Aceptable`, `Bueno`, `Insatisfactorio`, `Sobresaliente` *(+5 more)* |
| **DES_DominioContenidos**<br>`fldLLSEBJFrNvQwWp` | `number` | Numeric field |  |
| **DES_DominioContenidosTxt**<br>`fldzvFCTyA82PfeJP` | `singleSelect` | Single choice dropdown | `Excelente`, `Bueno`, `Sobresaliente`, `Domina cabalmente los contenidos de la clase`, `Se le nota inseguro(a) y debe recurrir a material de apoyo` *(+1 more)* |
| **DES_TrabajanEnProducto**<br>`fldiTxBBcNJOCS1jd` | `number` | Numeric field |  |
| **DES_TrabajanEnProductoTxt**<br>`fldAMRy00GfhLcjJs` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Básico`, `Trabajan pero el tiempo es breve y/o resultado es poco claro`, `La clase se reparte más o menos igual entre escucharlo(a) y trabajar` *(+3 more)* |
| **DES_CuantosMinutosTrabajando**<br>`fldWZYrBMTIJjhnWA` | `number` | Numeric field |  |
| **DES_MinutosTrabajando_pp**<br>`fldC9VYsuBRZC08ZM` | `formula` | Calculated field | Formula: `IF(
  {fldcsJcKyi4BG9z75}!=0,
  100 * {fldWZYrBM...` |
| **DES_MinutosTrabajandoCalif**<br>`fldsfGYPEdxyFTRi1` | `number` | Numeric field |  |
| **DES_MinutosTrabajandoCalifTxt**<br>`fldsJ18UaztmJ1Obs` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `No aplica, no hay NEE en este curso`, `Deficiente` *(+8 more)* |
| **DES_DaOportunidadDeExplorar**<br>`fldXt2J3xwtepv1Bu` | `number` | Numeric field |  |
| **DES_DaOportunidadDeExplorarTxt**<br>`fldjws2BrNJdKqN9X` | `singleSelect` | Single choice dropdown | `Aceptable`, `Deficiente`, `Bueno`, `Excelente`, `Insatisfactorio` *(+8 more)* |
| **DES_MonitoreaOrienta**<br>`fldZ6R3O72vjun6jE` | `number` | Numeric field |  |
| **DES_MonitoreaOrientaTxt**<br>`fldvfJ1MAByVPxWCi` | `singleSelect` | Single choice dropdown | `Deficiente`, `Bueno`, `Aceptable`, `Sobresaliente`, `Básico` *(+4 more)* |
| **DES_TodosTrabajan**<br>`fldapmUCY9D70Yr7h` | `number` | Numeric field |  |
| **DES_TodosTrabajanTxt**<br>`flddQERWAoXoAwyuV` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Deficiente`, `Excelente`, `Básico` *(+6 more)* |
| **DES_MasTrabajoEncargoAdelantados**<br>`fldQmXCPOeRThFwsw` | `number` | Numeric field |  |
| **DES_MasTrabajoEncargoAdelantadosTxt**<br>`fldZiLEQioVv96qq1` | `singleSelect` | Single choice dropdown | `No, los que terminan antes aprovechan el tiempo a su elección`, `Sí, les encarga ayudar a compañeros(as)`, `Sí, les entrega material adicional a medida que terminan`, `No, los que terminan antes se quedan "de brazos cruzados"`, `Sí, tiene preparadas actividades complementarias` *(+4 more)* |
| **DES_SabeAdaptarParaNEE**<br>`flduRfYIZ9sECZMu5` | `number` | Numeric field |  |
| **DES_SabeAdaptarParaNEETxt**<br>`fldrwPtcs7DiMZ0Cd` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `No aplica, no hay NEE en este curso`, `Deficiente` *(+5 more)* |
| **DES_ActividadesVariadas**<br>`fldJMMr23Vyrb03Ee` | `number` | Numeric field |  |
| **DES_ActividadesVariadasTxt**<br>`fldPwkHkOZPC8MJVO` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `No aplica, no hay NEE en este curso`, `Deficiente` *(+4 more)* |
| **DES_PensamientoCritico**<br>`fld1ThlbrK8D2YZvk` | `number` | Numeric field |  |
| **DES_PensamientoCriticoTxt**<br>`fldZ28IrbUo9B8ZKr` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `No aplica, no hay NEE en este curso`, `Deficiente` *(+6 more)* |
| **DES_AutonomiaResponsabilidad**<br>`fldy2gQw83ykoy6cf` | `number` | Numeric field |  |
| **DES_AutonomiaResponsabilidadTxt**<br>`fldSNNZkb9Fu7UaER` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `No aplica, no hay NEE en este curso`, `Deficiente` *(+7 more)* |
| **DES_EvaluaFormativamente**<br>`fldmJr8y69zwx99jp` | `number` | Numeric field |  |
| **DES_EvaluaFormativamenteTxt**<br>`fldXseIuFWs7Pym3b` | `singleSelect` | Single choice dropdown | `Evalúa sin retroalimentaciones`, `Sí, lo hace a lo largo de la clase, entregando retroalimentaciones valiosas y significativas`, `Evalúa pero da retroalimentaciones pobres`, `No realiza evaluaciones formativas a lo largo de la clase` |
| **DES_EscuchaValora**<br>`fldOlChoOztzsxF6p` | `number` | Numeric field |  |
| **DES_EscuchaValoraTxt**<br>`fldMoSX6H5GbIEX8r` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `No aplica, no hay NEE en este curso`, `Deficiente` *(+5 more)* |
| **DES_TratoRespetoCordial**<br>`fldFTua08ZQP93IPt` | `number` | Numeric field |  |
| **DES_TratoRespetoCordialTxt**<br>`fldbn5P5DRVzr0x2s` | `singleSelect` | Single choice dropdown | `Aceptable`, `Excelente`, `Bueno`, `Sobresaliente`, `Básico` *(+3 more)* |
| **DES_TratoPorNombre**<br>`fldu3fiLCaJbmwMhZ` | `number` | Numeric field |  |
| **DES_TratoPorNombreTxt**<br>`fldSmlDJl8tpZAcLn` | `singleSelect` | Single choice dropdown | `A algunos`, `A unos pocos`, `A Algunos(as)`, `A bastantes`, `A todos(as)` |
| **DES_MantieneAmbiente**<br>`fldy10smqzrIuCSXj` | `number` | Numeric field |  |
| **DES_MantieneAmbienteTxt**<br>`fldBWrO9ajC7sch2n` | `singleSelect` | Single choice dropdown | `Excelente`, `Bueno`, `Básico`, `Sobresaliente`, `Logra un ambiente razonablemente bueno` *(+3 more)* |
| **DES_PreguntaTodos**<br>`fld3PfoQ3BotrpGL2` | `number` | Numeric field |  |
| **DES_PreguntaTodosTxt**<br>`fldmuvOBVjeAgllVg` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Aceptable`, `Excelente`, `Llega a buena parte del curso` *(+3 more)* |
| **DES_ConstruyeDesdeElError**<br>`fldzpxNp3hXDnT79t` | `number` | Numeric field |  |
| **DES_ConstruyeDesdeElErrorTxt**<br>`fldpQS2xclP77wk7X` | `singleSelect` | Single choice dropdown | `Deficiente`, `Excelente`, `Bueno`, `Aceptable`, `Insatisfactorio` *(+6 more)* |
| **DES_FelicitaPequenosLogros**<br>`fldQRJN8koQ0Z4uWU` | `number` | Numeric field |  |
| **DES_FelicitaPequenosLogrosTxt**<br>`fldxdhCGanQLnsPUd` | `singleSelect` | Single choice dropdown | `Bueno`, `Sobresaliente`, `Excelente`, `Insatisfactorio`, `Bastante` *(+3 more)* |
| **DES_IntervieneProntamenteConvivencia**<br>`fldmkYt1hPEsyXwRq` | `number` | Numeric field |  |
| **DES_IntervieneProntamenteConvivenciaTxt**<br>`fldHN2OG7XaDRl7Qu` | `singleSelect` | Single choice dropdown | `Aceptable`, `No fue necesario en esta clase`, `Deficiente`, `Básico`, `Sobresaliente` *(+4 more)* |
| **DES_AplicaNormativaCriteriosamente**<br>`fldXnokWioyTEgDhg` | `number` | Numeric field |  |
| **DES_AplicaNormativaCriteriosamenteTxt**<br>`fldHxxIwkIqWsBsZb` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Insatisfactorio`, `No fue necesario en esta clase`, `Sobresaliente` *(+5 more)* |
| **DES_TieneRecursosManejoCurso**<br>`fld8beaKuEgi75BcZ` | `number` | Numeric field |  |
| **DES_TieneRecursosManejoCursoTxt**<br>`fldOSpEYPGz7UgBIt` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `Básico`, `Sobresaliente` *(+3 more)* |
| **DES_ValoraSolucionesNovedosas**<br>`fldb42vK7lHUjwq5L` | `number` | Numeric field |  |
| **DES_ValoraSolucionesNovedosasTxt**<br>`fldQCEbwNkksgwA5J` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `Básico`, `Sobresaliente` *(+4 more)* |
| **DES_SuperadoDisciplina**<br>`fld0w4oHLVdqnvHzA` | `number` | Numeric field |  |
| **DES_SuperadoDisciplinaTxt**<br>`fld8yeFmu0qkk0awN` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `Básico`, `Sobresaliente` *(+2 more)* |
| **DES_ModelaEmpatia**<br>`fld8bb9UWmfUgR8LN` | `number` | Numeric field |  |
| **DES_ModelaEmpatiaTxt**<br>`fldUFtw1j2k4K82eX` | `singleSelect` | Single choice dropdown | `Bueno`, `Aceptable`, `Excelente`, `Básico`, `Sobresaliente` *(+5 more)* |
| **DES_UsaApoyoAudiovisual**<br>`fldbIWrzNBbVbFzhP` | `singleSelect` | Single choice dropdown | `Sí,  en mayor parte de la clase`, `Sí,  sólo como apoyo secundario`, `No` |
| **DES_ApoyoAudiovisualEsAporte**<br>`fldynAV9rkdBnV10c` | `number` | Numeric field |  |
| **DES_ApoyoAudiovisualEsAporteTxt**<br>`fldStKDnEeGw0eq2k` | `singleSelect` | Single choice dropdown | `Bueno`, `Deficiente`, `Sobresaliente`, `Se perdería valor pero se podría hacer bien sin el apoyo audiovisual`, `Ayuda, pero resulta más bien distractivo y/o contraproducente, que un aporte` *(+2 more)* |
| **INGL_PoneOrdenEnIngles**<br>`fld6pfgM5dj5zQS8V` | `number` | Numeric field |  |
| **INGL_PoneOrdenEnInglesTxt**<br>`fld6Hzib2pkMYNn9t` | `singleSelect` | Single choice dropdown | `Luego de unas primeras frases en Español, continua en Inglés`, `Desde que entra, los ordena y da instrucciones en Inglés` |
| **INGL_SiEstudianteConsultaEnIngles**<br>`fldHbliR1vG4yfBtc` | `number` | Numeric field |  |
| **INGL_SiEstudianteConsultaEnInglesTxt**<br>`fld8XiRFerJ0kHNl8` | `singleSelect` | Single choice dropdown | `Le habla en Inglés motivándolo(a) a preguntar también en Inglés`, `Combina Español con Inglés` |
| **INGL_DocenteInglesTodaLaClase**<br>`fldbRA52hLE5s8gOg` | `number` | Numeric field |  |
| **INGL_DocenteInglesTodaLaClaseTxt**<br>`fldyTTRpQQcOstufo` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **INGL_EstudiantesInglesTodaLaClase**<br>`fldvKwaxoqB4LXJz7` | `number` | Numeric field |  |
| **INGL_EstudiantesInglesTodaLaClaseTxt**<br>`fld41RxAbH18a38As` | `singleSelect` | Single choice dropdown | `Algunos, motivados por el(la) docente`, `Casi siempre, hacen buenos esfuerzos`, `Muy pocos o ninguno` |
| **PB_TonoVoz**<br>`fldP9hv7Z4t3xosWA` | `number` | Numeric field |  |
| **PB_TonoVozTxt**<br>`fldkHraTA8EwGJOqm` | `singleSelect` | Single choice dropdown | `Sí, habla normal`, `A veces lo infantiliza` |
| **PB_AsistenteValorAgregado**<br>`fldk4Rlep8X7VdYeQ` | `number` | Numeric field |  |
| **PB_AsistenteValorAgregadoTxt**<br>`fldKTnIfQJS08Wid1` | `singleSelect` | Single choice dropdown | `Sí`, `Excelente`, `Aceptable`, `Bueno`, `Sin ella la clase no sería posible` *(+2 more)* |
| **PB_AsistenteConocePlan**<br>`fld3WA6ryP967MZ35` | `number` | Numeric field |  |
| **PB_AsistenteConocePlanTxt**<br>`fldwtw7Z4Bwz2j8gc` | `singleSelect` | Single choice dropdown | `Sí`, `Aceptable`, `Deficiente`, `Bueno`, `Se anticipa preparando lo necesario para darle continuidad y más valor a la clase; hacen gran equipo con la Educadora` *(+3 more)* |
| **PB_Autonomia**<br>`fld1drP7FJt4A5GLl` | `number` | Numeric field |  |
| **PB_AutonomiaTxt**<br>`fld9PrmcwxnafotMi` | `singleSelect` | Single choice dropdown | `Sí`, `Deficiente`, `Básico`, `Toman decisiones pero se les deja cambiarlas`, `Cada actividad tiene al menos una opción que deben elegir y hacerse cargo de su elección` *(+1 more)* |
| **PB_NoSustituir**<br>`fldVrYB2GLXbAUcSf` | `number` | Numeric field |  |
| **PB_NoSustituirTxt**<br>`fldSamYKgquJVKXnp` | `singleSelect` | Single choice dropdown | `Sí`, `Aceptable`, `Básico`, `No, y los(las) animan a realizar las acciones cuando piden ayuda para algo que pueden realizar por su cuenta`, `Los(las) sustituyen en cosas que parecen difíciles para los(las) niños(as)` |
| **CIE_TerminaATiempo**<br>`fldbICuNErLe9hbrd` | `number` | Numeric field |  |
| **CIE_TerminaATiempoTxt**<br>`fldw5sL852oqEipDC` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **CIE_LogroObjetivo**<br>`fldOouLOqDzvDc43K` | `number` | Numeric field |  |
| **CIE_LogroObjetivoTxt**<br>`fldG9SOWC8OJL58zv` | `singleSelect` | Single choice dropdown | `Se cumplió pobremente`, `Se cumplió sólo parcialmente`, `Se cumplió completamente`, `Se excedió sobre el objetivo`, `No se cumplió` *(+1 more)* |
| **CIE_RealizaActCierre**<br>`fldYG45dzLbO1uhZM` | `number` | Numeric field |  |
| **CIE_RealizaActCierretxt**<br>`fldHYEFG9hr2Cu9cp` | `singleSelect` | Single choice dropdown | `Sí, pero se percibe una vaga improvisación`, `Sí, de manera destacada con unos pocos`, `No hay actividad de cierre`, `Sí, de manera destacada con todos` |
| **CIE_ReflexionMetaCognicion**<br>`fldMuTfhrCc4p2oEf` | `number` | Numeric field |  |
| **CIE_ReflexionMetaCognicionTxt**<br>`fldx4zwo77p9MgVOS` | `singleSelect` | Single choice dropdown | `Aceptable`, `Excelente`, `Bueno`, `Deficiente`, `Insatisfactorio` *(+7 more)* |
| **CIE_AmbienteAdecuado**<br>`fldW7vn5XuQXD9qB1` | `number` | Numeric field |  |
| **CIE_AmbienteAdecuadoTxt**<br>`fldJvcqcAcCWiT96Z` | `singleSelect` | Single choice dropdown | `Hay bastante desorden con poco manejo de el(la) docente`, `Algunos trabajan, otros hacen cosas ajenas a la clase`, `Sí, todos trabajan activamente` |
| **COM_IndividualGrupal**<br>`fldUYobCIh1YgdWve` | `singleSelect` | Single choice dropdown | `Trabajo individual`, `Trabajo en pares`, `Trabajo en grupos de tres o más`, `Trabajo combinado, personal y grupal` |
| **COM_ActividadDescripcion**<br>`fldloYS1dlIqhRJF8` | `multilineText` | Multi-line text |  |
| **COM_Fortalezas**<br>`fldOEPqlW63ZTKMvR` | `multilineText` | Multi-line text |  |
| **COM_Debilidades**<br>`fldDlYiESZihPdnEf` | `multilineText` | Multi-line text |  |
| **COM_ObsParaProfesorJefe**<br>`fld0o8sOtW37uN1Y6` | `multilineText` | Multi-line text |  |
| **COM_ComReservados**<br>`fld5JnD0Ni2jYqiDt` | `multilineText` | Multi-line text |  |
| **ValorNivelGlobalClase**<br>`flde6Kpjzj8GtMgMT` | `number` | Numeric field |  |
| **NivelGlobalClaseTxt**<br>`fldptutFjopYdRbiX` | `singleSelect` | Single choice dropdown | `Básico`, `Bueno`, `Excelente`, `Aceptable`, `Sobresaliente` *(+1 more)* |
| **ComportamientoEstudiantesValor**<br>`fldDGh1x591jTUlqI` | `number` | Numeric field |  |
| **ComportamientoEstudiantesTxt**<br>`fldEK8YysFYVYEF1G` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Básico`, `Insatisfactorio` |
| **TrabajoEstudiantesValor**<br>`fldofgMhxXorKY53s` | `number` | Numeric field |  |
| **TrabajoEstudiantesTxt**<br>`fld8inKVkaexG573P` | `singleSelect` | Single choice dropdown | `Básico`, `Insatisfactorio`, `Sobresaliente`, `Bueno` |
| **ValorCumplimientoAnterior**<br>`fldcHwDSDFBT3jKzR` | `number` | Numeric field |  |
| **CumplimientoAnteriorTxt**<br>`fld3fZnN0cY4yJwQG` | `singleSelect` | Single choice dropdown | `Básico`, `Bueno`, `Sobresaliente` |
| **FirmaEvaluador**<br>`fldqety6zcZSgYWdB` | `multipleAttachments` | Type: multipleAttachments |  |
| **PDF1docente**<br>`fld7yK1nSYwfe302Z` | `multipleAttachments` | Type: multipleAttachments |  |
| **PDF1docenteOK**<br>`fldts11V4VNASxVXC` | `number` | Numeric field |  |
| **FlagCamposA010_OK**<br>`fld2p0FRDkGEssDx0` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fld0UTjgTSsrHI2dX}>0,
    {fldK...` |
| **PDF1docenteyEvalEmailOK**<br>`fldvbSklREmXXvryu` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fld7yK1nSYwfe302Z} !="",
    {f...` |
| **PDF1evaluador**<br>`fldXlMymhqJ7bYHtd` | `multipleAttachments` | Type: multipleAttachments |  |
| **INEXIA_A010_AparatoUsado**<br>`fldgtHacUkFaYsvD5` | `singleSelect` | Single choice dropdown | `Computador`, `Celular`, `Tablet` |
| **INEXIA_A010_ExperienciaLlenado**<br>`fldkN2QAM34Zao7gd` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Básico`, `Insatisfactorio` |
| **INEXIA_A010_HaySugerencia**<br>`fld0kmVNyBwBSp6s2` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **INEXIA_A010_TipoDeSugerencia**<br>`fldsUl8feWquWmRkn` | `singleSelect` | Single choice dropdown | `Sugerencia de mejora`, `Consulta de soporte` |
| **INEXIA_A010_SugerenciaPrioridad**<br>`fldBYWhSZV81uRX8o` | `singleSelect` | Single choice dropdown | `Necesario, sería bueno tenerlo pronto`, `Deseable, para la próxima versión`, `Urgente, lo necesitamos lo antes posible`, `Ninguna prioridad, es sólo una idea o comentario` |
| **EdicionRegistro**<br>`fldGFLzk9LZkwMms0` | `createdTime` | Auto-generated creation time |  |
| **VersionFormA012**<br>`fld4FxWx76ogwLWk7` | `singleLineText` | Type: singleLineText |  |
| **FEEDB_Fecha**<br>`fldnAO4XWFuw045JK` | `date` | Date |  |
| **FEEDB_CoordinacionTxt**<br>`fldb8z8NHSl0NriC5` | `singleSelect` | Single choice dropdown | `Él(ella) preguntó por la fecha con interés genuino`, `Aceptó y cumplió la primera fecha propuesta`, `Costó agendarla, estuvo esquivo(a)`, `Sin motivo válido, no se presentó a la fecha acordada y hubo que reagendar` |
| **FEEDB_CoordinacionValor**<br>`fldkbftNi2bVJ49uk` | `formula` | Calculated field | Formula: `SWITCH({fldb8z8NHSl0NriC5},
	"Él(ella) preguntó p...` |
| **FEEDB_DijoFortalezasTxt**<br>`fldlVtuErX9N1HSxV` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **FEEDB_DijoFortalezasValor**<br>`fld2C4LAkTqwIPlNh` | `formula` | Calculated field | Formula: `SWITCH({fldlVtuErX9N1HSxV},
	"Sí",4,
	"No",1
)...` |
| **FEEDB_RespuestaAlFeedbackTxt**<br>`fldiVmlUwZ1InAyET` | `singleSelect` | Single choice dropdown | `Agradecido(a) y constructivo(a)`, `Con interés`, `Indiferente`, `Con desdén` |
| **FEEDB_RespuestaAlFeedbackValor**<br>`fldU5YtfGQAkl0o7g` | `formula` | Calculated field | Formula: `SWITCH({fldiVmlUwZ1InAyET},
	"Agradecido(a) y con...` |
| **FEEDB_CompromisoMejoraTxt**<br>`fldidykG4XJ1AKqKi` | `singleSelect` | Single choice dropdown | `Comprometido(a) e ilusionado(a)`, `Comprometido(a)`, `Débilmente comprometido(a)`, `No se percibe compromiso` |
| **FEEDB_CompromisoMejoraValor**<br>`fldBKGMCJUupfDi7R` | `formula` | Calculated field | Formula: `SWITCH({fldidykG4XJ1AKqKi},
	"Comprometido(a) e i...` |
| **FEEDB_PromedioDocente**<br>`fldlYP5VeLCZtqpcq` | `formula` | Calculated field | Formula: `ROUND(
  (
    ({fldkbftNi2bVJ49uk}+
     {fldU...` |
| **FEEDB_EjeMejora**<br>`fld3rXKJJwpJILnI1` | `singleSelect` | Single choice dropdown | `Planificación y preparación`, `Estrategias pedagógicas`, `Gestión de aula y convivencia`, `Relación con los estudiantes`, `Evaluación y retroalimentación` *(+2 more)* |
| **FEEDB_UrgenciaMejora**<br>`fld48XcEdkrnC3CQT` | `singleSelect` | Single choice dropdown | `Es urgente, no es aceptable que no incorpore las sugerencias`, `Es necesario que mejore en los próximos meses`, `Es suficiente con que lo logre dentro del año o comienzo del siguiente` |
| **FEEDB_PlanDeAccion**<br>`fldTBONZNuYRPelIY` | `multilineText` | Multi-line text |  |
| **FEEDB_Comentarios**<br>`fldtnJUNMyk69ePxU` | `multilineText` | Multi-line text |  |
| **Flag_Enviar_Alarma**<br>`fld9Bc9ULXaffUSJp` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldsgSZ1fnXENtuvj}=0,
    {fldE...` |
| **INEXIA_FEEDB_Aparato**<br>`fldyCuo8GU5MgHdPQ` | `singleSelect` | Single choice dropdown | `Celular`, `Tablet`, `Computador` |
| **INEXIA_FEEDB_Experiencia**<br>`fldzFIx7EXXpzsA92` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Básico`, `Insatisfactorio` |
| **INEXIA_FEEDB_HaySugerencia**<br>`fldubTguEB7OmSkF7` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **INEXIA_FEEDB_Sugerencias**<br>`fld8mkX0QOg3a7gI9` | `multilineText` | Multi-line text |  |
| **INEXIA_FEEDB_Sugerencia_urgencia**<br>`flda7JSfHKUeEfoj4` | `singleSelect` | Single choice dropdown | `Urgente`, `Necesario`, `Deseable`, `Ninguna` |
| **INEXIA_FEEDB_ValorGuionIA**<br>`fldUHMDzECgw7GkTR` | `singleSelect` | Single choice dropdown | `Muy bueno, una ayuda excelente para la calidad de la entrevista`, `Bueno, facilita la entrevista`, `Algo ayuda, pero no mucho`, `No me sirvió` |
| **INEXIA_FEEDB_SugerenciaGuion**<br>`fldUQ52PSNkkkxl7r` | `singleLineText` | Type: singleLineText |  |
| **Hay_entrevista**<br>`fldsgSZ1fnXENtuvj` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldb8z8NHSl0NriC5}!="",
    {fl...` |
| **HayEntrevFEEDB**<br>`fldCMmlVGsnzB9QMk` | `formula` | Calculated field | Formula: `IF(
  {fldsgSZ1fnXENtuvj}=1,"Sí","No"
)` |
| **Docentes**<br>`fldGisyKhnKWQBESg` | `singleLineText` | Type: singleLineText |  |
| **OAentrevistasFeedback**<br>`fld6jwvR0dvo7hF2e` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ObservacionesAulaPorEje**<br>`fldPCZ9F1p60HsOca` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **RecordId**<br>`fld2CZs2rxVr8HaNI` | `formula` | Calculated field | Formula: `RECORD_ID()` |
| **FEEDB_url_FormA012**<br>`fldsHKBcZCyfvmACn` | `formula` | Calculated field | Formula: `'https://web.miniextensions.com/5Ri0P6iQjMctee9K40...` |
| **EjeMejoraANTERIOR**<br>`fld9bsooGzexU80qW` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **PlanDeAccionANTERIOR**<br>`fld0KxTZXGHbeSLHG` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **UrgenciaMejoraANTERIOR**<br>`fldh4xp81khEXplnc` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **LogoColegio**<br>`fldujZRvrWE5qelz1` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ValoracionAvanceANTERIOR**<br>`fldizZlHUUQtr5J5L` | `singleSelect` | Single choice dropdown | `Sobresaliente`, `Bueno`, `Básico`, `Insatisfactorio` |
| **AvanceANTERIORvalor**<br>`fldnY1NADpeuctmNX` | `number` | Numeric field |  |
| **FechaANTERIOR**<br>`fldsRXEkxpF7BIQ0S` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FEEDB_PlanDeAccion copy**<br>`fldzFDnW1CEQN5n01` | `multilineText` | Multi-line text |  |
| **ColegioPrincipal**<br>`fldFLr4jilOkltnVM` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **DocenteEmail**<br>`fldJmFOQcYOkgDuHI` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Region**<br>`fldUgggzRLAXnIFvl` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioComuna**<br>`flduIWlGHKmxMCOwv` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **RBD**<br>`fldLQZveVDzJUfNfb` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **RectorNombre**<br>`flduPMZtPBUYRn1yY` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **EducacionDelValorVigenteTxt**<br>`fld74olsktzNsCXGf` | `singleSelect` | Single choice dropdown | `No aplica en este nivel`, `Cuando exige a los(las) estudiantes, usa casi siempre el valor como justificación`, `A veces usa el valor para respaldar una exigencia`, `Lo usa en la exigencia pero incorrectamente`, `A veces explica el valor, pero no exige vivirlo` *(+1 more)* |
| **EducacionDelValorVigente**<br>`fld9s1yWmvYTFokFM` | `number` | Numeric field |  |
| **PB_AprovechanErrores**<br>`fldjyJvB9IbGouOKP` | `number` | Numeric field |  |
| **PB_AprovechanErroresTxt**<br>`fld62m9wGcLpG3lAh` | `singleSelect` | Single choice dropdown | `Sí`, `Deficiente`, `Básico`, `Dejan el error como referencia pero le sacan poco provecho`, `Evitan borrar sus errores para que los descubran, y repitan la acción usándolo como referencia` |
| **VersionFormA010Novedades**<br>`fldHBUHbeJ565faIo` | `singleLineText` | Type: singleLineText |  |
| **MacroVersionNovedades**<br>`fld0q1eiyleTGLq0h` | `singleLineText` | Type: singleLineText |  |
| **Flag1**<br>`fldh2CjWd4BgtUGFB` | `singleLineText` | Type: singleLineText |  |
| **Flag2**<br>`fld9hCVTZOnPwN5Dh` | `singleLineText` | Type: singleLineText |  |
| **Anterior-acuerdos**<br>`fld3bZOdzkObM39LF` | `multilineText` | Multi-line text |  |
| **Anterior-fecha**<br>`fldw6jOdPZKkiABy3` | `singleLineText` | Type: singleLineText |  |
| **Anterior-urgencia**<br>`fld6KYBMgKZzTJQh0` | `singleLineText` | Type: singleLineText |  |
| **Anterior-evaluador**<br>`fldCcgvu409mB8i7T` | `singleLineText` | Type: singleLineText |  |
| **Anterior-eje**<br>`fldrYEkREQlietm5t` | `singleLineText` | Type: singleLineText |  |
| **Docentes 2**<br>`fldAJNmrfcYONA08N` | `singleLineText` | Type: singleLineText |  |
| **MisObservaciones**<br>`fld5HPrUQVSxkAGzy` | `singleLineText` | Type: singleLineText |  |
| **DIMENSION1_PROM**<br>`fldswqimY02k9z3hx` | `formula` | Calculated field | Formula: `ROUND(
  ({fldXOuE9IP3JjiBLS}+{fldaOGBJvViiAbmCn}...` |
| **Dim1-1**<br>`fldXOuE9IP3JjiBLS` | `number` | Numeric field |  |
| **Dim1-2**<br>`fldaOGBJvViiAbmCn` | `number` | Numeric field |  |
| **Dim1-3**<br>`fldfeJ0cr36McHhMW` | `number` | Numeric field |  |
| **Dim1-4**<br>`fldh0UOiSsFH4mQdH` | `number` | Numeric field |  |
| **Dim1-5**<br>`fldGn6nxUtpQp4vk5` | `number` | Numeric field |  |
| **Dim2-1**<br>`flda19wf90yxrRsDK` | `number` | Numeric field |  |
| **Dim2-2**<br>`fldxxz4BYBA0GNyaK` | `number` | Numeric field |  |
| **Dim2-3**<br>`fldNRYXMMu9z1kq7i` | `number` | Numeric field |  |
| **Dim2-4**<br>`fldfuMZECncEHMeEL` | `number` | Numeric field |  |
| **Dim2-5**<br>`fldfVzITM7lmwSXRd` | `number` | Numeric field |  |
| **Dim3-1**<br>`fldJDTAqM3UmsG4sF` | `number` | Numeric field |  |
| **Dim3-2**<br>`fldDsyo9XPUEqYbay` | `number` | Numeric field |  |
| **Dim3-3**<br>`fldFXaaYR7EfeFQIZ` | `number` | Numeric field |  |
| **Dim3-4**<br>`fldcRodajk2cfH4vF` | `number` | Numeric field |  |
| **Dim3-5**<br>`fldZrxyGmft0g69Xh` | `number` | Numeric field |  |
| **DIM1-PROM**<br>`fldBVqZNnJdn9OsXK` | `formula` | Calculated field | Formula: `IF(
  ({fldXOuE9IP3JjiBLS}+{fldaOGBJvViiAbmCn}+{f...` |
| **DIM2-PROM**<br>`fldfUNgqNnifH1qeT` | `formula` | Calculated field | Formula: `IF(
  ({flda19wf90yxrRsDK}+{fldxxz4BYBA0GNyaK}+{f...` |
| **DIM3-PROM**<br>`fld1iVTWUrf6QDlzB` | `formula` | Calculated field | Formula: `IF(
  ({fldJDTAqM3UmsG4sF}+{fldDsyo9XPUEqYbay}+{f...` |
| **Electivo**<br>`fldAy8YUQxKTwHpUk` | `singleLineText` | Type: singleLineText |  |
| **FEEDB_url_FormA012_Fillout**<br>`fldQsmVBBYF0FIuov` | `formula` | Calculated field | Formula: `"https://forms.fillout.com/t/tZ7L19a5kius?id=" & R...` |
| **ObservacionesAulaPorEje copy**<br>`fldXgDYtVwb2cQHDJ` | `singleLineText` | Type: singleLineText |  |
| **Ahora**<br>`fldFZdIr5hIYJzEO5` | `formula` | Calculated field | Formula: `NOW()` |

---

## 📋 26. ObsAulaClasificacionCampos

*Table ID: `tblhi7K4aQxrVBptH`*
*Fields: 23*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **CampoNombre**<br>`fldVRDll47gi1cK3u` | `singleLineText` | Type: singleLineText |  |
| **Num**<br>`fldjj0mjFGjWSwDVC` | `autoNumber` | Type: autoNumber |  |
| **PreguntaA010**<br>`fldysL3CrmDDn5lSI` | `richText` | Rich text with formatting |  |
| **Opciones**<br>`fldMqzNkxweyhUPH1` | `richText` | Rich text with formatting |  |
| **Dim1-1**<br>`fld3uYT8rZyeTykws` | `checkbox` | True/False checkbox |  |
| **Dim1-2**<br>`fldGmIxP0ICoCM06W` | `checkbox` | True/False checkbox |  |
| **Dim1-3**<br>`fldGibZsKsSlCENFG` | `checkbox` | True/False checkbox |  |
| **Dim1-4**<br>`fldcMyWLR8JTOTWuv` | `checkbox` | True/False checkbox |  |
| **Dim1-5**<br>`fldJSvTdPqBbpN7AG` | `checkbox` | True/False checkbox |  |
| **Dim2-1**<br>`fldpb5MRpbXr1jYTn` | `checkbox` | True/False checkbox |  |
| **Dim2-2**<br>`fldcTinDskwQwReU8` | `checkbox` | True/False checkbox |  |
| **Dim2-3**<br>`fldAQQvyTyJzydfvw` | `checkbox` | True/False checkbox |  |
| **Dim2-4**<br>`fldtBnptMxVQA3sM0` | `checkbox` | True/False checkbox |  |
| **Dim2-5**<br>`fldBNzWNRuI3Y62OP` | `checkbox` | True/False checkbox |  |
| **Dim3-1**<br>`fld1b4lpAkEXZfPSR` | `checkbox` | True/False checkbox |  |
| **Dim3-2**<br>`fldyWyEqvbIilG9oM` | `checkbox` | True/False checkbox |  |
| **Dim3-3**<br>`fldnKFwnZtpjh3L0i` | `checkbox` | True/False checkbox |  |
| **Dim3-4**<br>`fldcGRM7X3eughB3s` | `checkbox` | True/False checkbox |  |
| **Dim3-5**<br>`fld6rnQ3FTlPWP2Mg` | `checkbox` | True/False checkbox |  |
| **Campania**<br>`fldOOPTSzlcI2BRmq` | `checkbox` | True/False checkbox |  |
| **FinCampania**<br>`fldyonaojP8GxdujL` | `date` | Date |  |
| **UltModificacion**<br>`fldlWu3Qs3pL45V4M` | `lastModifiedTime` | Auto-generated modification time |  |
| **VersionA020**<br>`fldw0iI6qIUayQXBu` | `singleLineText` | Type: singleLineText |  |

---

## 📋 27. ObservacionesAulaPorCampo

*Table ID: `tblD12MY3AU7z1gmg`*
*Fields: 20*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Serial**<br>`fldbKbK6ZQ0HVhF7s` | `autoNumber` | Type: autoNumber |  |
| **NumeroObsAula**<br>`fldlhl4muSp5inA48` | `number` | Numeric field |  |
| **NumeroObsAulaLookUp**<br>`fldi5xNrhXvNbCxd1` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ColegioTag**<br>`fldwBnZDNJcpER7YZ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **CicloTag**<br>`fldGRasMA7p2N38Dh` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaTxt**<br>`fldys7XoF45cOH9ii` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Curso**<br>`fldPI9LVFvljNGCv3` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **DocenteTag**<br>`fldIzYbpTMUPc8k29` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Asignatura**<br>`fldqwkpGpqqOuSqEB` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Electivo**<br>`fld316UBOT558f2In` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Trimestre**<br>`fldGXn15BqnqBFyYZ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Departamento**<br>`fldrI4TGoRkM2JazX` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **CampoConcepto**<br>`fldZvTOk7X4HHBU0M` | `singleLineText` | Type: singleLineText |  |
| **CampoValor**<br>`fld5Q73xUWOGWkZZW` | `singleLineText` | Type: singleLineText |  |
| **NivelObservadoValor**<br>`fldKdOKGqOfhCSURa` | `number` | Numeric field |  |
| **CampoTxt**<br>`fldGw4gOy6pwcBamR` | `singleLineText` | Type: singleLineText |  |
| **NivelObservadoTxt**<br>`fld6ikQHnCDqtG0V0` | `singleLineText` | Type: singleLineText |  |
| **NivelObservadoTag**<br>`fld3SkK2zaNq535Ni` | `singleSelect` | Single choice dropdown | `Llega apenas toca`, `Lo logra con gestos y pocas palabras`, `Algunos reaccionan`, `Logra un buen ambiente de trabajo`, `Logra ordenar y disponer al grupo sin decir una palabra` *(+158 more)* |
| **version9002v2**<br>`fldTrkF4D7M13DaHt` | `singleLineText` | Type: singleLineText |  |
| **flagDePaso**<br>`fldzHXtRxfF3JZMbe` | `number` | Numeric field |  |

---

## 📋 28. ObsAulaModelosDashboard

*Table ID: `tblKQDCcIsgPH0TFq`*
*Fields: 5*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EjeNumero**<br>`flddyIMMWSNvlugTW` | `number` | Numeric field |  |
| **EjeNombre**<br>`fldJHWE8htNZrxnBI` | `singleLineText` | Type: singleLineText |  |
| **Aspecto**<br>`fldpg8uFrDWOUox2A` | `singleLineText` | Type: singleLineText |  |
| **Modelo**<br>`fld2NwkxORCaW5GAH` | `singleLineText` | Type: singleLineText |  |
| **ObservacionesAulaPorModelo**<br>`fldKRV9ytNNBcu0ca` | `singleLineText` | Type: singleLineText |  |

---

## 📋 29. AULAS_PROGRESO

*Table ID: `tblwVY1r7GiCMibTK`*
*Fields: 12*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Rec**<br>`fld4oxmGuzaqeg4WK` | `autoNumber` | Type: autoNumber |  |
| **Anio**<br>`fld8dK9CO1MALGcvB` | `number` | Numeric field |  |
| **Mes**<br>`fldw1uP7MKHA3qRfN` | `number` | Numeric field |  |
| **Trim-Sem**<br>`fld57STroctKbqpU5` | `number` | Numeric field |  |
| **NombreKPI**<br>`fldzkPxgB1tXzN0Tg` | `singleLineText` | Type: singleLineText |  |
| **Colegio**<br>`fldGGjPPKDYG1ozx4` | `singleLineText` | Type: singleLineText |  |
| **RUTdocente**<br>`fldOqTuxVGUEtVcaR` | `number` | Numeric field |  |
| **RUTestudiante**<br>`fldvaQR6LrCrZizHu` | `number` | Numeric field |  |
| **Asignatura**<br>`fldzIQR3dwYROxQoI` | `singleLineText` | Type: singleLineText |  |
| **Curso**<br>`fldHp6CuG6eDl6UiR` | `singleLineText` | Type: singleLineText |  |
| **VALOR**<br>`fldXRnyLPHxcanSJL` | `number` | Numeric field |  |
| **VALORtxt**<br>`fldEgt1byrla8cE0q` | `singleLineText` | Type: singleLineText |  |

---

## 📋 30. OAentrevistasFeedback

*Table ID: `tblQOHVg3iN5xw3TN`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Id**<br>`fldqFHHnf9u8yJPEH` | `autoNumber` | Type: autoNumber |  |
| **NumeroOA**<br>`fldXJ6Rc8JECbq1Yj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **OrganizacionSigla**<br>`fldRVO3aDMB4uSFmC` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ColegioSigla**<br>`flduK6caxHOkggnsG` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **ObsAulaTipo**<br>`fldxAhlYQILzWBKZF` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaOA**<br>`fldWpOgyItBo153PX` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Docente**<br>`fld7olTqYbP7hIGyy` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Evaluador**<br>`fldUu1zpY5DeWzNdL` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **GuionSugerido**<br>`fldJhCz47Swd9xgAb` | `multilineText` | Multi-line text |  |
| **FechaFeedBack**<br>`fldGkcKHelamQiOWQ` | `singleLineText` | Type: singleLineText |  |

---

## 📋 31. PARAMETROS_GENERALES

*Table ID: `tblHh5JH2mlsWBh6v`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Registro**<br>`fldvtLM1raXT6cres` | `number` | Numeric field |  |
| **TipoParametro**<br>`fldJLDTz9ck7Q8kS6` | `singleLineText` | Type: singleLineText |  |
| **UmbralStopDiagnostico5B**<br>`fld8xTS4NopOIb1Jy` | `number` | Numeric field |  |
| **UmbralStopDiagnostico6B**<br>`fldtlmS1j9CjklEBF` | `number` | Numeric field |  |
| **UmbralStopDiagnostico7B**<br>`fldkoxxrYAGtJY91a` | `number` | Numeric field |  |
| **UmbralStopDiagnostico8B**<br>`fld8u4LPaB0XUb4VA` | `number` | Numeric field |  |
| **Estudiantes**<br>`fldEMt3EjtkcKuEW7` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ParamUrl**<br>`fld4rsEgUTAEXnaDz` | `url` | URL link |  |
| **ParamDescripcion**<br>`fldi5DQeZyGTV1sTw` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes copy**<br>`fldGM4ptHbfZsBgrb` | `singleLineText` | Type: singleLineText |  |

---

## 📋 32. PreguntasDiagnostico

*Table ID: `tbl1PkngaTAfGYhpv`*
*Fields: 71*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **NumeroPregunta**<br>`fld3lKashVhxRiu4C` | `autoNumber` | Type: autoNumber |  |
| **Nivel**<br>`fldZChyhaGxGsqt92` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **NivelTxt**<br>`fldMIX7wC4dK64hvR` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **NivelTxtTag**<br>`fldBfE79sqd1vngJb` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Materia**<br>`fldbILOsLcBaboqFJ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **MateriaTag**<br>`fldo6MHPaqtTEvIl5` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TipoPreguntaJF**<br>`fldDuw0NptPHUsWfC` | `singleLineText` | Type: singleLineText |  |
| **PreguntaActiva**<br>`flddwVDjGbQfHYK2x` | `singleLineText` | Type: singleLineText |  |
| **Eje**<br>`fldyXht7nd1FOyK8C` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **EjeTag**<br>`flds2gj0ABVEvOPB2` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **RespuestaCorrecta**<br>`fld151Rq2R2UxFilS` | `formula` | Calculated field | Formula: `IF(
  {fldDuw0NptPHUsWfC}="control_radio",
  IF(...` |
| **RespuestaCorrectaOriginal**<br>`fldRGPAqanBBVNwto` | `singleLineText` | Type: singleLineText |  |
| **FlagAuditarRespuesta**<br>`fldjOgdBTO3Z62lb2` | `number` | Numeric field |  |
| **AuditoriaRespuesta**<br>`fldkJ6qA1yyRFQQtu` | `singleLineText` | Type: singleLineText |  |
| **validaAuto**<br>`fldqVuwynZyZ1fdsJ` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldXdExcVWvUccBgk}!="", {fld2JjY...` |
| **AuditoriaExplicacion**<br>`fldLKE8tRcsnjnYHn` | `singleLineText` | Type: singleLineText |  |
| **VersionProc2014aud**<br>`fldxJWJ3VdajEhatD` | `singleLineText` | Type: singleLineText |  |
| **AuditoriaModelo**<br>`fldiYSisacYy359HD` | `singleLineText` | Type: singleLineText |  |
| **FechaProc2014aud**<br>`fldCQtJG5fXI08W6q` | `singleLineText` | Type: singleLineText |  |
| **JustificacionExpertos**<br>`fldOzeSyc1Wt6ZTBa` | `singleLineText` | Type: singleLineText |  |
| **versionTablaPreguntasDiagnostico**<br>`fldlqMtDChd5PO8IP` | `singleLineText` | Type: singleLineText |  |
| **Origen**<br>`fldXdExcVWvUccBgk` | `singleLineText` | Type: singleLineText |  |
| **ModeloIA**<br>`fldxKDiSRgWTbU2tM` | `singleLineText` | Type: singleLineText |  |
| **ParametrosIA**<br>`fldnocJ4MMiGV6KRf` | `singleLineText` | Type: singleLineText |  |
| **VersionCreaPreguntas**<br>`fld6Vufh6VsNyfqsi` | `singleLineText` | Type: singleLineText |  |
| **OA**<br>`fld2JjYbPufKkl337` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **TempAPI**<br>`flduKJhcSVmtjwU5b` | `number` | Numeric field |  |
| **OAdescripcion**<br>`fldA8ZOYL6Whqf8zb` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **RespuestaIA**<br>`fldlbJ0mtkNg87ft2` | `singleLineText` | Type: singleLineText |  |
| **Pregunta**<br>`fldUVLEeBhIAUXHHk` | `multilineText` | Multi-line text |  |
| **PreguntaTxT**<br>`fld7rmpxwNpePFBkt` | `singleLineText` | Type: singleLineText |  |
| **Opciones**<br>`fldc9Q2pUlV8F7EqN` | `multilineText` | Multi-line text |  |
| **OpcionesBonitas**<br>`fldlPcRoDTvkEL4zI` | `formula` | Calculated field | Formula: `"A."&LEFT(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE({fldc9Q...` |
| **OpcionesBonitasParaHTML**<br>`fldfRx5RHPmxulz7R` | `formula` | Calculated field | Formula: `LEFT(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE({fldc9Q2pUlV...` |
| **OpcionesSinLetra**<br>`fldrWZJSlEuzZtnX2` | `formula` | Calculated field | Formula: `CONCATENATE(
  MID({fldc9Q2pUlV8F7EqN},3,FIND("|"...` |
| **PreguntaRevisada**<br>`fldc7GVzsHpEcLlqY` | `singleLineText` | Type: singleLineText |  |
| **OA2**<br>`fldQuws9z33btNBmY` | `singleLineText` | Type: singleLineText |  |
| **IncluirParaJF**<br>`fld7edbrO8o3XCNZj` | `number` | Numeric field |  |
| **IncluidaEnJF**<br>`fldroHGNUFkZQ2weP` | `singleLineText` | Type: singleLineText |  |
| **VersionProc2015**<br>`fldPKtUWzD4hfnfJ2` | `singleLineText` | Type: singleLineText |  |
| **FechaProc2015**<br>`fldLxQTpeNq8h8SrH` | `singleLineText` | Type: singleLineText |  |
| **MateriaAbreviado**<br>`fldAlRQA1AaeO3qJc` | `formula` | Calculated field | Formula: `SWITCH({fldbILOsLcBaboqFJ},
  "Matemática","Mate"...` |
| **Nivel2**<br>`fldZioxtgwHvAbubc` | `singleSelect` | Single choice dropdown | `5`, `6`, `7`, `8` |
| **TipoPregunta**<br>`fldq9nKoLD9ZRPjTT` | `singleSelect` | Single choice dropdown | `Respuesta única`, `Alternativas` |
| **Validation**<br>`fldnimPDwItqzEm1m` | `singleLineText` | Type: singleLineText |  |
| **Figura**<br>`fldfTSlCAt9ZHJZTg` | `singleLineText` | Type: singleLineText |  |
| **ConFigura**<br>`fldn7BmqTvQ8VtGYD` | `checkbox` | True/False checkbox |  |
| **Trigger**<br>`fld6FSLacUl49Cq3c` | `checkbox` | True/False checkbox |  |
| **FechaCreacionPregunta**<br>`fldgPcIeM3zYLSg9q` | `createdTime` | Auto-generated creation time |  |
| **Relevancia**<br>`fldO03KTljFMCJOZz` | `number` | Numeric field |  |
| **CalcularDificultad**<br>`flduzOxHHtD1LlP2w` | `number` | Numeric field |  |
| **Dificultad**<br>`fld5m4mimQRxWYCsT` | `number` | Numeric field |  |
| **DificultadRango**<br>`fldMmCbVbXryKHWNF` | `formula` | Calculated field | Formula: `IF({fld2Q98HRxOiOyRme} != "v20250315",
  IF(
   ...` |
| **JustificacionDificultad**<br>`fld75JoavuZ7uxP5o` | `singleLineText` | Type: singleLineText |  |
| **Version2014CalculaDificultad**<br>`fldfvyezVlJto1eNq` | `singleLineText` | Type: singleLineText |  |
| **ApiCohereStatus**<br>`fld2Q98HRxOiOyRme` | `singleLineText` | Type: singleLineText |  |
| **FechaCalifDificultad**<br>`fld4JDt0MS7JLSobV` | `singleLineText` | Type: singleLineText |  |
| **Diversidad**<br>`fldwu3jaNoXzIvZ8l` | `number` | Numeric field |  |
| **PertinenciaAlOA**<br>`fldbhNtYYmYdLRdgA` | `number` | Numeric field |  |
| **LinkMiniE-EditarPreguntas**<br>`fldWlNbWple6qOC5E` | `formula` | Calculated field | Formula: `'https://web.miniextensions.com/eagbbcwGLugG5KN2ki...` |
| **FechaRevisiónPregunta**<br>`fld9QyHXixXs5joVf` | `dateTime` | Date and time |  |
| **UsuarioRevisor**<br>`fldiTpMqW2dnXxpfx` | `singleLineText` | Type: singleLineText |  |
| **ComentarioRevision**<br>`fldoI4qoEFhlztIm4` | `singleLineText` | Type: singleLineText |  |
| **RevisorIP**<br>`fldnhjyxKykquMxbj` | `singleLineText` | Type: singleLineText |  |
| **RevisorLatitud**<br>`fld2oy3S2DhhLrAO7` | `singleLineText` | Type: singleLineText |  |
| **RevisorLongitud**<br>`fld3vLdLlWPdAEbOC` | `singleLineText` | Type: singleLineText |  |
| **Creada**<br>`fldIOL8M762TfuJW5` | `createdTime` | Auto-generated creation time |  |
| **Modificada**<br>`fldrKfrvek2TedR8Z` | `lastModifiedTime` | Auto-generated modification time |  |
| **Curriculum**<br>`fldcgZUHoxc8hDfNH` | `singleLineText` | Type: singleLineText |  |
| **OA copy**<br>`fldNrowLQqR06rWWR` | `singleLineText` | Type: singleLineText |  |
| **RespuestasDiagnostico2**<br>`fldoYuszTNssucve7` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 33. PruebasDiagnostico

*Table ID: `tbllHdmG8RQwFgkNq`*
*Fields: 11*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **CodigoPruebaDiagnostico**<br>`fldmImhDPj8laj7VX` | `autoNumber` | Type: autoNumber |  |
| **CantidadPreguntas**<br>`fld17rplJuHPLdrdw` | `number` | Numeric field |  |
| **Nivel**<br>`fld3DNgBdaUAQYLRO` | `singleLineText` | Type: singleLineText |  |
| **Materia**<br>`fldl66pHMv12ShcOp` | `singleLineText` | Type: singleLineText |  |
| **ValidacionAutomatica**<br>`fld4Jf0sXDexvmo4Z` | `singleLineText` | Type: singleLineText |  |
| **FechaCreacionPrueba**<br>`flde2PMDPHIoMRvSy` | `createdTime` | Auto-generated creation time |  |
| **HTMLpruebaDiag**<br>`fldC1eJHKB7rSbWzd` | `multilineText` | Multi-line text |  |
| **urlPruebaDiagnostico**<br>`fldIGNgK7pELPwN8n` | `url` | URL link |  |
| **Version2015**<br>`fldT7PTFfXrSvACcn` | `singleLineText` | Type: singleLineText |  |
| **RespuestasDiagnostico2**<br>`fldphpQE4T0mV0h0G` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **CreadoMisTarea**<br>`flda7gaGC5zWtnNQ7` | `number` | Numeric field |  |

---

## 📋 34. RecursosMultimedia

*Table ID: `tblmtWNh65TZmdZFX`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID**<br>`fldFqY2Rechs2LYmb` | `autoNumber` | Type: autoNumber |  |
| **Nombre**<br>`fldGeIpqJXrf2CKHO` | `singleLineText` | Type: singleLineText |  |
| **url**<br>`fldehnTdyw6MsihWV` | `url` | URL link |  |
| **Hash**<br>`fldRNF8ulsMAAQGyl` | `singleLineText` | Type: singleLineText |  |
| **Tipo**<br>`fldsJRHgTk9Sz0ByZ` | `singleLineText` | Type: singleLineText |  |
| **Formato**<br>`fld1YZBN0CSkMkIfD` | `singleLineText` | Type: singleLineText |  |
| **Origen**<br>`fldF2CCCLVGHCKdln` | `singleLineText` | Type: singleLineText |  |
| **FechaGeneracion**<br>`fldc6RBj2oJxhXIiM` | `singleLineText` | Type: singleLineText |  |
| **TasaUso**<br>`fldQMjzoVgU5rBQMX` | `number` | Numeric field |  |
| **Metadata**<br>`fldrSBGkplzR3UQmB` | `singleLineText` | Type: singleLineText |  |

---

## 📋 35. RespaldosExpertos-A010

*Table ID: `tblyLZnQcs25wPQaf`*
*Fields: 3*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Rec**<br>`fld4QFQqQJfo8XLsu` | `autoNumber` | Type: autoNumber |  |
| **Pregunta**<br>`fldyZw200NMgSCoOG` | `richText` | Rich text with formatting |  |
| **RespaldosExpertos**<br>`fldnASYwpM331NRNH` | `richText` | Rich text with formatting |  |

---

## 📋 36. RespuestasDiagnostico

*Table ID: `tblF02FEQa8SahxG7`*
*Fields: 51*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTestudiante**<br>`fld2dcDCzxomxxXrf` | `singleLineText` | Type: singleLineText |  |
| **PruebaCodigo**<br>`fldP1xPmoAORu6iyh` | `singleLineText` | Type: singleLineText |  |
| **PruebaVersion**<br>`fldjN3yuGPcZAmwF4` | `singleLineText` | Type: singleLineText |  |
| **FechaRecepcion**<br>`fldEi6IL0nXXn5HUv` | `createdTime` | Auto-generated creation time |  |
| **CantPreguntas**<br>`fldzuULscy1NRTaYV` | `number` | Numeric field |  |
| **Duracion**<br>`fldX3XNrq1byhv6X8` | `singleLineText` | Type: singleLineText |  |
| **MinutosMinimos**<br>`fld1MyvWi3QnOeovd` | `number` | Numeric field |  |
| **AlarmaPocoTiempo**<br>`fldRvjzUcoV7egwCv` | `formula` | Calculated field | Formula: `IF(
  VALUE(
    MID({fldX3XNrq1byhv6X8},0,FIND(...` |
| **ComoTeFue**<br>`fldoOREpJQu6BQYXy` | `singleLineText` | Type: singleLineText |  |
| **1**<br>`fldjRbJmZeQuG8163` | `singleLineText` | Type: singleLineText |  |
| **2**<br>`fldTwXPyXi1ykq9wC` | `singleLineText` | Type: singleLineText |  |
| **3**<br>`fld499FQGE2Te4XY3` | `singleLineText` | Type: singleLineText |  |
| **4**<br>`fldhd5zsU2a30Nvvh` | `singleLineText` | Type: singleLineText |  |
| **5**<br>`fldNxg9haRXDZV7OR` | `singleLineText` | Type: singleLineText |  |
| **6**<br>`fldSNItXM8m3bOmux` | `singleLineText` | Type: singleLineText |  |
| **7**<br>`fldFlwVH1h3ByVvai` | `singleLineText` | Type: singleLineText |  |
| **8**<br>`fld6jssaspNjtlqTs` | `singleLineText` | Type: singleLineText |  |
| **9**<br>`fldWeN3nI37J8dEd4` | `singleLineText` | Type: singleLineText |  |
| **10**<br>`fld4PRE8e8tDvVCNC` | `singleLineText` | Type: singleLineText |  |
| **11**<br>`fldEwphWw8zQpy6NY` | `singleLineText` | Type: singleLineText |  |
| **12**<br>`fldKku1EItuyZW5o6` | `singleLineText` | Type: singleLineText |  |
| **13**<br>`fld6DF16dKuf0gv3k` | `singleLineText` | Type: singleLineText |  |
| **14**<br>`fldlJ8a7iaahEEbju` | `singleLineText` | Type: singleLineText |  |
| **15**<br>`fldGKycKvTw7LylmU` | `singleLineText` | Type: singleLineText |  |
| **16**<br>`fldmxgMalGDPrADv0` | `singleLineText` | Type: singleLineText |  |
| **17**<br>`fld3ftNCDdJAv6SaT` | `singleLineText` | Type: singleLineText |  |
| **18**<br>`fldkaQVVNDSds47Dx` | `singleLineText` | Type: singleLineText |  |
| **19**<br>`fldOD62wKDSlhHOOR` | `singleLineText` | Type: singleLineText |  |
| **20**<br>`fldoSk8DEMVS8qFYz` | `singleLineText` | Type: singleLineText |  |
| **21**<br>`fldkAhlEJbrJzRm1p` | `singleLineText` | Type: singleLineText |  |
| **22**<br>`fldTMsybiFGQG5USe` | `singleLineText` | Type: singleLineText |  |
| **23**<br>`fldYkXlExizWxKF35` | `singleLineText` | Type: singleLineText |  |
| **24**<br>`fldo08Cmat3cr1QZx` | `singleLineText` | Type: singleLineText |  |
| **25**<br>`fld5l4OPMkxLUAeGt` | `singleLineText` | Type: singleLineText |  |
| **26**<br>`fldpGosMtmV3WD4kl` | `singleLineText` | Type: singleLineText |  |
| **27**<br>`fldvDZDtFBVoHNImJ` | `singleLineText` | Type: singleLineText |  |
| **28**<br>`flduHcJ5XFPjFJEHK` | `singleLineText` | Type: singleLineText |  |
| **29**<br>`fldvUekXdvA8Sxquv` | `singleLineText` | Type: singleLineText |  |
| **30**<br>`fld9N6mblUHzg4sdE` | `singleLineText` | Type: singleLineText |  |
| **31**<br>`fldNqNDrpE1emDdzW` | `singleLineText` | Type: singleLineText |  |
| **32**<br>`fldmQgJnmVBH9yqEU` | `singleLineText` | Type: singleLineText |  |
| **33**<br>`fldqsFZxVEF8nVD9p` | `singleLineText` | Type: singleLineText |  |
| **34**<br>`fldvXvLKRH8ntrRqa` | `singleLineText` | Type: singleLineText |  |
| **35**<br>`fldXE22X7HBlLxVQg` | `singleLineText` | Type: singleLineText |  |
| **36**<br>`fldFdtV1CaoTsMy48` | `singleLineText` | Type: singleLineText |  |
| **37**<br>`fldjJ4tNp4gwSXYb3` | `singleLineText` | Type: singleLineText |  |
| **38**<br>`fldhf1gNGjjsGJaB8` | `singleLineText` | Type: singleLineText |  |
| **39**<br>`fldo4ddhlQpzcxXlE` | `singleLineText` | Type: singleLineText |  |
| **40**<br>`fldd1G7BWBR7qkL6J` | `singleLineText` | Type: singleLineText |  |
| **Procesado**<br>`fldP85YDZUrZR6G2z` | `number` | Numeric field |  |
| **FechaProcesado**<br>`fldNaGplR8d0SriXB` | `singleLineText` | Type: singleLineText |  |

---

## 📋 37. RespuestasDiagnostico2

*Table ID: `tbljP5KSSPFsQez1C`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTestudiante**<br>`fldsps15owYH7CcmD` | `singleLineText` | Type: singleLineText |  |
| **FlagCopiadoAbrechasPorEstudiante**<br>`fldjfYV9u1mKlKAi6` | `number` | Numeric field |  |
| **PruebaCodigo**<br>`fld7qjDXRUyV25jWi` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **PruebaCodigo2**<br>`fldvIMycz2xAqKHEC` | `singleLineText` | Type: singleLineText |  |
| **FechaDiagnostico**<br>`fldDyL6pJ0OLjm7xj` | `createdTime` | Auto-generated creation time |  |
| **PreguntaId**<br>`fldjx4L5uOr9MTCiI` | `singleLineText` | Type: singleLineText |  |
| **PreguntaIdLookUp**<br>`flddKNMF9YRDA4FMs` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **OA**<br>`fldvMY6VnyugFHEJS` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **AprobadaReprobada**<br>`fld35S6j0FyQdcYVf` | `number` | Numeric field |  |
| **VersionWebHook2015aux**<br>`fldfJfBlskPmXTahy` | `singleLineText` | Type: singleLineText |  |

---

## 📋 38. RespuestasMotivacion

*Table ID: `tblqnhPM5cVZt5MT5`*
*Fields: 62*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTestudiante**<br>`fldNArNKOzbtQlcEd` | `singleLineText` | Type: singleLineText |  |
| **PruebaVersion**<br>`fld4aiICVRZ6TaLS2` | `singleLineText` | Type: singleLineText |  |
| **FechaRecepcion**<br>`fldpFlSTfpK4GTW7t` | `createdTime` | Auto-generated creation time |  |
| **Duracion**<br>`fldIqcXzF3YFAjla6` | `singleLineText` | Type: singleLineText |  |
| **1**<br>`fld4eqTuegDBZWgj1` | `singleLineText` | Type: singleLineText |  |
| **2**<br>`fldETcZGckOFDeoJA` | `singleLineText` | Type: singleLineText |  |
| **3**<br>`fldPwoPYVGP0xScb1` | `singleLineText` | Type: singleLineText |  |
| **4**<br>`fld2AkJA94XajBKIf` | `singleLineText` | Type: singleLineText |  |
| **TotalReconocimiento**<br>`fldxXPqLTYKEnyWqa` | `formula` | Calculated field | Formula: `{fld4eqTuegDBZWgj1}+{fldETcZGckOFDeoJA}+{fldPwoPYV...` |
| **5**<br>`fldyUvjppTKKiJm1P` | `singleLineText` | Type: singleLineText |  |
| **6**<br>`fldDaXD51a9auCBHv` | `singleLineText` | Type: singleLineText |  |
| **7**<br>`fldqIL5PgjQIRJKng` | `singleLineText` | Type: singleLineText |  |
| **8**<br>`fldRGHCiHrAqM9F6q` | `singleLineText` | Type: singleLineText |  |
| **TotalLogroPersonal**<br>`fldJtobiLYuUdwBpi` | `formula` | Calculated field | Formula: `{fldyUvjppTKKiJm1P}+{fldDaXD51a9auCBHv}+{fldqIL5Pg...` |
| **9**<br>`fldHB2dvX5UQr1Tq2` | `singleLineText` | Type: singleLineText |  |
| **10**<br>`fldPc6OgtagKOJR0A` | `singleLineText` | Type: singleLineText |  |
| **11**<br>`fldpTEr4LamXIml0W` | `singleLineText` | Type: singleLineText |  |
| **12**<br>`fldvHJbMXvhFiKkB4` | `singleLineText` | Type: singleLineText |  |
| **TotalCuriosidad**<br>`fldafU3MTr5HgDtpu` | `formula` | Calculated field | Formula: `{fldHB2dvX5UQr1Tq2}+{fldPc6OgtagKOJR0A}+{fldpTEr4L...` |
| **13**<br>`fldR0UbesMhmj4Kgi` | `singleLineText` | Type: singleLineText |  |
| **14**<br>`fld66nkfxcXoXsqws` | `singleLineText` | Type: singleLineText |  |
| **15**<br>`fldr7NmSKVje4mAzS` | `singleLineText` | Type: singleLineText |  |
| **16**<br>`fld7UvWiAIqWKoSIY` | `singleLineText` | Type: singleLineText |  |
| **TotalInteresPractico**<br>`fldl5g6OlUYzCVXJD` | `formula` | Calculated field | Formula: `{fldR0UbesMhmj4Kgi}+{fld66nkfxcXoXsqws}+{fldr7NmSK...` |
| **17**<br>`fldOCIXKSfwHOU7nR` | `singleLineText` | Type: singleLineText |  |
| **18**<br>`fld5x5532FFkLSmQv` | `singleLineText` | Type: singleLineText |  |
| **19**<br>`fldz0lcEZFFsAv31P` | `singleLineText` | Type: singleLineText |  |
| **20**<br>`fld9fziLTOIZreUbx` | `singleLineText` | Type: singleLineText |  |
| **TotalRelacionesSociales**<br>`fldf97TiiBKBVoAJn` | `formula` | Calculated field | Formula: `{fldOCIXKSfwHOU7nR}+{fld5x5532FFkLSmQv}+{fldz0lcEZ...` |
| **21**<br>`fld5XwvMYdeQSFBen` | `singleLineText` | Type: singleLineText |  |
| **22**<br>`fldE9HIjxHtXZT95c` | `singleLineText` | Type: singleLineText |  |
| **23**<br>`fldJHcvMMkm3QyUg3` | `singleLineText` | Type: singleLineText |  |
| **24**<br>`fld9nnMupvQjKP5cv` | `singleLineText` | Type: singleLineText |  |
| **TotalAutonomia**<br>`fldRiAaptaDW79Hdv` | `formula` | Calculated field | Formula: `{fld5XwvMYdeQSFBen}+{fldE9HIjxHtXZT95c}+{fldJHcvMM...` |
| **25**<br>`fldQIjYX1mkSdotTr` | `singleLineText` | Type: singleLineText |  |
| **26**<br>`flda3DCUIoIafrjxj` | `singleLineText` | Type: singleLineText |  |
| **27**<br>`fldg0eNBUDIv0BXzH` | `singleLineText` | Type: singleLineText |  |
| **28**<br>`fldf4rTdcHCqYxTUI` | `singleLineText` | Type: singleLineText |  |
| **TotalCompetividad**<br>`fldrls8pbisNea9y7` | `formula` | Calculated field | Formula: `{fldQIjYX1mkSdotTr}+{flda3DCUIoIafrjxj}+{fldg0eNBU...` |
| **29**<br>`fld7g8paT5zOr6sKn` | `singleLineText` | Type: singleLineText |  |
| **30**<br>`fldX8AdTvaH6X3EWK` | `singleLineText` | Type: singleLineText |  |
| **31**<br>`fld5MBXiJH0EDaOPE` | `singleLineText` | Type: singleLineText |  |
| **32**<br>`fld6ZazupvdwB7arD` | `singleLineText` | Type: singleLineText |  |
| **33**<br>`fldscNyqsoAK1pkFP` | `singleLineText` | Type: singleLineText |  |
| **34**<br>`fldQxKAf7x5jMcFEt` | `singleLineText` | Type: singleLineText |  |
| **35**<br>`fldP4FgEyCbg2uVQR` | `singleLineText` | Type: singleLineText |  |
| **36**<br>`fldZ1uljvXbRnr124` | `singleLineText` | Type: singleLineText |  |
| **37**<br>`fldRZHlAfX7BXdRj9` | `singleLineText` | Type: singleLineText |  |
| **38**<br>`fldyOHCqCe6xJfRF0` | `singleLineText` | Type: singleLineText |  |
| **39**<br>`fldh9GFJgXgdgDVM5` | `singleLineText` | Type: singleLineText |  |
| **40**<br>`fldWkBrwd3819rKfb` | `singleLineText` | Type: singleLineText |  |
| **41**<br>`fldPJm8DH45y0GINA` | `singleLineText` | Type: singleLineText |  |
| **42**<br>`fldcMskMIRXybpe8o` | `singleLineText` | Type: singleLineText |  |
| **43**<br>`fld1NJ0EhIjVy62u8` | `singleLineText` | Type: singleLineText |  |
| **44**<br>`fldV2h0Main8ARnl8` | `singleLineText` | Type: singleLineText |  |
| **45**<br>`fldBRd0FyDEPtRDZf` | `singleLineText` | Type: singleLineText |  |
| **46**<br>`fldwydh3eyiAzcPEp` | `singleLineText` | Type: singleLineText |  |
| **47**<br>`fldPB87TwasZpmWVi` | `singleLineText` | Type: singleLineText |  |
| **48**<br>`fldX6U6FvgfkNAbCX` | `singleLineText` | Type: singleLineText |  |
| **Total_Amotivacion**<br>`fldq1D0ttoXRr3tC7` | `formula` | Calculated field | Formula: `{fld7g8paT5zOr6sKn}+{fldX8AdTvaH6X3EWK}+{fld5MBXiJ...` |
| **Procesado**<br>`fldAvk8LeWe6aUVfx` | `number` | Numeric field |  |
| **FechaProcesado**<br>`fldyxVzt6a07bfxaz` | `singleLineText` | Type: singleLineText |  |

---

## 📋 39. Sostenedores

*Table ID: `tblbmUkhsg7NuMecj`*
*Fields: 4*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **RUTsostenedor**<br>`fldUCj5Er6C2DXdAk` | `singleLineText` | Type: singleLineText |  |
| **RUTsostenedorLookup**<br>`fldcmojvhQnDfNhYX` | `singleLineText` | Type: singleLineText |  |
| **sostenedorNombre**<br>`fldTpsdYwJQ0Ew7Qe` | `singleLineText` | Type: singleLineText |  |
| **Colegios**<br>`fldmsYGdpg0uwhzrM` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 40. TicketSoporte

*Table ID: `tblUN79PV2Y3Dmmbt`*
*Fields: 13*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **NumTicket**<br>`fldMJnOfOziRSKlm3` | `autoNumber` | Type: autoNumber |  |
| **NumOA**<br>`fld4s4i8Yu9XpuzvB` | `number` | Numeric field |  |
| **FechaTicket**<br>`fldr0q5RIkptZzD1W` | `createdTime` | Auto-generated creation time |  |
| **Colegio**<br>`fldG1Xj1G4LY13Mvb` | `singleLineText` | Type: singleLineText |  |
| **App**<br>`fldF2CDqxWBfbQvk2` | `singleLineText` | Type: singleLineText |  |
| **Form**<br>`fldRLCjQ7YS4oTKw3` | `singleLineText` | Type: singleLineText |  |
| **VersionForm**<br>`fldAMpfhkYiidHNT1` | `singleLineText` | Type: singleLineText |  |
| **TipoSugerencia**<br>`fldN1tAkhtsWpxxWZ` | `singleLineText` | Type: singleLineText |  |
| **User**<br>`fldqAeOGGkMGyEsZX` | `singleLineText` | Type: singleLineText |  |
| **EmailUser**<br>`fldmW8PpjRQ5hBHUh` | `email` | Email address |  |
| **TicketSolicitud**<br>`fldoqoqq5hNrLEKhJ` | `multilineText` | Multi-line text |  |
| **TicketUrgencia**<br>`fldsNgYmMfR9zbEyt` | `singleSelect` | Single choice dropdown | `Reclamo`, `Urgente`, `Necesario en próxima versión`, `Deseable cuando se pueda`, `Es sólo una idea` *(+4 more)* |
| **FechaResuelto**<br>`fldm9G0On22J9s7cG` | `date` | Date |  |

---

## 📋 41. TIPS dev

*Table ID: `tblVY1lZpF8BkzY9R`*
*Fields: 5*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Rec**<br>`fld7fK7MeJCszRRSh` | `autoNumber` | Type: autoNumber |  |
| **Plataforma**<br>`fldmdqCLS2XIKiu9u` | `singleLineText` | Type: singleLineText |  |
| **Uso**<br>`fldgSBQ8kNrT2lK1b` | `singleLineText` | Type: singleLineText |  |
| **Tip**<br>`fldnSHZFKs7pUKnB6` | `multilineText` | Multi-line text |  |
| **Detalles**<br>`fld2K4ofJp2GW03kM` | `multilineText` | Multi-line text |  |

---

## 📋 42. UsuariosWeb

*Table ID: `tblC6M3v61Es0vWqk`*
*Fields: 27*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EmailUsuario**<br>`fldLBorx51RCJm1aL` | `email` | Email address |  |
| **ColegioPrincipal**<br>`fldLRyFMxCiCrrOOS` | `singleLineText` | Type: singleLineText |  |
| **Password**<br>`fldeAQMTsqVFC2FCz` | `singleLineText` | Type: singleLineText |  |
| **Flag1000**<br>`fldPvQohyZB9puXG4` | `number` | Numeric field |  |
| **PasswordHash**<br>`fldmpD3UVbVSO2LFw` | `singleLineText` | Type: singleLineText |  |
| **RUT**<br>`fldAjMApAlDoFOHWg` | `singleLineText` | Type: singleLineText |  |
| **EmailCalculado**<br>`fldOWagD0A8T7TPro` | `formula` | Calculated field | Formula: `{fldLBorx51RCJm1aL}` |
| **UserRol**<br>`fldXwWKaAn9JQuaFp` | `singleLineText` | Type: singleLineText |  |
| **RUTusuario**<br>`fldMIvoreei3DSmu1` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **estudianteColegio**<br>`fldt6BrDE2ObPCh2E` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **MiAviso**<br>`fldEZRkJyXFxvhWxk` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **colegioNombre**<br>`fldal9xyx2WwmsaM9` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteSexo**<br>`fldXfvMDdXUx5fzW9` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **estudianteNombreConpleto**<br>`fld1akEQngixiKA7V` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **UserNombreWeb**<br>`fldV9zpluLeVohCI0` | `singleLineText` | Type: singleLineText |  |
| **estudianteCursoActual**<br>`fld6X9CSqqHKwLzBM` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **UserFoto**<br>`fldsaKyk8dv8irlJF` | `multipleAttachments` | Type: multipleAttachments |  |
| **UserUltimoIngreso**<br>`fldMp1Wp41wVuotP0` | `dateTime` | Date and time |  |
| **UserCreacion**<br>`flda3JlGNsMS6WyKm` | `createdTime` | Auto-generated creation time |  |
| **UserUltimaEdicion**<br>`fldDZcTxCm0LiWdgf` | `lastModifiedTime` | Auto-generated modification time |  |
| **UserUserCreacion**<br>`flda1DI0ZS3gseAOz` | `createdBy` | Auto-generated creator |  |
| **UserUserEdicion**<br>`fld0ioqcliJWXJtWl` | `lastModifiedBy` | Auto-generated last editor |  |
| **UserActivo**<br>`fldE8TThY4AQnHD2o` | `checkbox` | True/False checkbox |  |
| **AccesoMagicLink**<br>`fldfqkPBi8JV2AdcG` | `url` | URL link |  |
| **Alondra**<br>`fldtaAg5PfB8Rw9tT` | `checkbox` | True/False checkbox |  |
| **Aulas**<br>`fldIcQr8AVsLKvC2Y` | `checkbox` | True/False checkbox |  |
| **Estudiantes copy**<br>`fldOI6KgCWdQlZYZ5` | `singleLineText` | Type: singleLineText |  |

---

## 📋 43. UsuariosMapeo

*Table ID: `tblngOGL1QfPjtmOD`*
*Fields: 5*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EmailUsuario**<br>`fldeO3HNehRud1m2h` | `email` | Email address |  |
| **App-url**<br>`fldaCCudm8HOLAsIb` | `url` | URL link |  |
| **Cliente**<br>`fld83RJ6d2eklmcdG` | `singleLineText` | Type: singleLineText |  |
| **Status**<br>`fldIZxOkbC7I8RTT7` | `singleSelect` | Single choice dropdown | `Activo`, `Inactivo` |
| **Creado**<br>`fld3RxXV9xdObBcyn` | `createdTime` | Auto-generated creation time |  |

---

## 📋 44. Videos

*Table ID: `tblagTryoDHEMVKD9`*
*Fields: 4*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **TipoVideo**<br>`fldQHFZkSI6HkwCti` | `singleLineText` | Type: singleLineText |  |
| **TituloVideo**<br>`fldgsH8H18gfndoq1` | `singleLineText` | Type: singleLineText |  |
| **URL_video**<br>`fldniB1RSk5NxEwHg` | `url` | URL link |  |
| **CaratulaVideo**<br>`fldsL93kl82jlUAGP` | `multipleAttachments` | Type: multipleAttachments |  |

---

## 🔄 About This Documentation

### 📋 Source Information
- **Base**: Aulas (`aulas`)
- **Base ID**: `appEuz3PoChgzMmCH`
- **Generated**: 2025-12-08 22:04:10

### 🛠️ Field Type Legend
- **singleSelect**: Dropdown with single choice
- **multipleSelects**: Dropdown with multiple choices
- **formula**: Automatically calculated value
- **lookup**: References records from another table
- **rollup**: Aggregates data from linked records

### 🔧 Usage Notes
1. **API Usage**: Always use the exact field names and IDs shown above
2. **Select Fields**: Use only the options listed for select fields
3. **Formula Fields**: Read-only, cannot be modified via API
4. **Linked Fields**: lookup and rollup fields reference other tables

### ⚡ Automation
This document is auto-generated by GitHub Actions.
**Update schedule**: Daily at 8:00 AM UTC
**Last sync**: 2025-12-08 22:04:10

---
*Documentation for Aulas base - Generated 2025-12-08 22:04:10*