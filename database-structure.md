# 🗂️ Airtable Database Structure - Default

> **Last update**: 2026-03-26 09:06:47
> **Base**: default (Default)
> **Auto-generated** - Do not edit manually

## 📊 Summary

- **Tables**: 24
- **Total fields**: 459
- **Base ID**: `app9c8iiAYRGxxhtH`

- **singleSelect fields**: 77
- **multipleSelects fields**: 8
- **number fields**: 46
- **date fields**: 16
- **formula fields**: 10

---

## 📋 1. Anuncios

*Table ID: `tbl10FRDQ38L8ZHCq`*
*Fields: 15*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Anuncio**<br>`fldbqxZaXF4sbksl5` | `autoNumber` | Type: autoNumber |  |
| **Titulo**<br>`fldMj0p9ObDHGkEP6` | `singleLineText` | Type: singleLineText |  |
| **Mensaje**<br>`fldOqI5zDcEOsB4OZ` | `multilineText` | Multi-line text |  |
| **Activo**<br>`fldKGafIyXrGO9FX4` | `checkbox` | True/False checkbox |  |
| **FechaExpiracion**<br>`fldKUsPxskd9c7A4x` | `date` | Date |  |
| **Repetible**<br>`fld5C6pVWBktnvcXW` | `checkbox` | True/False checkbox |  |
| **AplicaFreemium**<br>`fld9ZGoNW6TclvbVS` | `checkbox` | True/False checkbox |  |
| **AplicaPremiumPago**<br>`fld2pMuQraJgsIv7Z` | `checkbox` | True/False checkbox |  |
| **AplicaBecaColegio**<br>`fldI6uCoqAS1CKVGI` | `checkbox` | True/False checkbox |  |
| **AplicaBecaPersonal**<br>`fldRoYb5oxtV912JZ` | `checkbox` | True/False checkbox |  |
| **Paises**<br>`fldBpGgwSMnZ9CE7w` | `multipleSelects` | Multiple choice dropdown | `Bolivia`, `Ecuador`, `Chile`, `Perú`, `Colombia` |
| **Estudiante**<br>`flddG8URyfX8mOp7k` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EnviarEmail**<br>`fldBsb3LE7ENfIfx9` | `checkbox` | True/False checkbox |  |
| **EmailEnviadoEn**<br>`fld8ywjOSdZfbyW1f` | `dateTime` | Date and time |  |
| **CreadoEn**<br>`fldabiwW4dP7kfSmV` | `createdTime` | Auto-generated creation time |  |

---

## 📋 2. Brechas

*Table ID: `tblAHnHa5fHOPLATq`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Brecha**<br>`fldfVgj3QTW6zfzkM` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldYeKZLOTrmZx9jz` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Materia**<br>`fldy3Letyi5rUox6u` | `singleSelect` | Single choice dropdown | `Matemáticas`, `Lenguaje`, `Ciencias`, `Historia`, `Inglés` *(+4 more)* |
| **EjeTematico**<br>`flds8wKLPjZrn7gpb` | `singleSelect` | Single choice dropdown | `Álgebra`, `Números`, `Geometría`, `Vocabulario`, `Comprensión lectora` *(+3 more)* |
| **Contenido**<br>`fldHxwk5khjbwcS7J` | `singleLineText` | Type: singleLineText |  |
| **NivelOrigen**<br>`flduhyOCgeqbK1dIw` | `singleSelect` | Single choice dropdown | `5°B`, `6°B`, `7°B`, `8°B`, `1°M` *(+2 more)* |
| **Prioridad**<br>`fldfd60pZlnFkeZSS` | `singleSelect` | Single choice dropdown | `🔴 Crítica`, `🟡 Media`, `🟢 Baja` |
| **Cerrada**<br>`fldVei33OZ1RDBj1x` | `checkbox` | True/False checkbox |  |
| **CerradaEn**<br>`flde2ELbO9RRLneRu` | `dateTime` | Date and time |  |
| **DetectadaEn**<br>`fldh1cCu1VJ9P00ZK` | `createdTime` | Auto-generated creation time |  |

---

## 📋 3. CodigosBeca

*Table ID: `tblbJONkSMMSwwmh4`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Codigo**<br>`fldHomfihCqQgDxSC` | `singleLineText` | Type: singleLineText |  |
| **Tipo**<br>`fldnLXDsLH8JRO1Af` | `singleSelect` | Single choice dropdown | `BECA`, `Tester` |
| **UsosMaximos**<br>`fld69Ws9F38CdFFCO` | `number` | Numeric field |  |
| **UsosActuales**<br>`fldJWXbVuqOxfZhfA` | `number` | Numeric field |  |
| **FechaExpiracion**<br>`fldxTjF7VmSafvfku` | `date` | Date |  |
| **Activo**<br>`fldubNWCX1ZO2zvkX` | `checkbox` | True/False checkbox |  |
| **Descripcion**<br>`fldZhdWkoJrdRuE7g` | `singleLineText` | Type: singleLineText |  |
| **DescuentoPp**<br>`fldMtH7CUtxABSfdx` | `percent` | Percentage |  |
| **EnUso**<br>`fldxhvbEe07IOCi7X` | `checkbox` | True/False checkbox |  |
| **FechaPrimerUso**<br>`fldp6xx9q6AQNlJvt` | `dateTime` | Date and time |  |

---

## 📋 4. Conversaciones

*Table ID: `tblhw3b9VCVrJtDu1`*
*Fields: 29*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Conversacion**<br>`fldhpzpygAWASqIcm` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldsFM6LQCnmLIpev` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FechaAltaEstudiante**<br>`fldzwhZAcGxX19VAw` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TipoPuerta**<br>`fldfGrwAFFXcL5jos` | `singleSelect` | Single choice dropdown | `aprender`, `preparar-evaluacion`, `estudiar`, `mejorar-habitos`, `prepararme-paes` |
| **Titulo**<br>`fldNkHyWabgfGAThi` | `singleLineText` | Type: singleLineText |  |
| **MateriaPrincipal**<br>`fld6eG16Hs7av0euL` | `singleLineText` | Type: singleLineText |  |
| **TipoNEE**<br>`fldx65y33zQeiXOsi` | `singleLineText` | Type: singleLineText |  |
| **CantidadMensajes**<br>`fldQFSerbNJRUagkv` | `count` | Type: count |  |
| **CantidadMensajesFinal**<br>`fldNlONZcXOGV6s2M` | `number` | Numeric field |  |
| **Tokens**<br>`fldtCm0VWw3wvkt0V` | `rollup` | Rollup from linked records |  |
| **TokensFinal**<br>`fldaYGwxvLqtSFKws` | `number` | Numeric field |  |
| **CostoAPI**<br>`fldvidJST7G3PhaTs` | `rollup` | Rollup from linked records |  |
| **Resumen**<br>`fldLJbxM83Q7BLBfZ` | `multilineText` | Multi-line text |  |
| **FechaInicio**<br>`fldUuqJjygGEcscrS` | `createdTime` | Auto-generated creation time |  |
| **SemanaISO**<br>`fldT2n1sMu58ilaGM` | `singleLineText` | Type: singleLineText |  |
| **DiaSemanaInicio**<br>`fldbpEisAN1d2n4nm` | `formula` | Calculated field | Formula: `WEEKDAY(SET_TIMEZONE({fldUuqJjygGEcscrS}, 'America...` |
| **UltimoMensaje**<br>`fldwOV5yGkT0tiMj3` | `lastModifiedTime` | Auto-generated modification time |  |
| **Duracion**<br>`fld8K7xwvCEwgb64O` | `formula` | Calculated field | Formula: `DATETIME_DIFF({fldwOV5yGkT0tiMj3},{fldUuqJjygGEcsc...` |
| **Activa**<br>`fldCvt5WUCe8du9JG` | `checkbox` | True/False checkbox |  |
| **TipoFin**<br>`fldscUy5JHcZ2gtIW` | `singleSelect` | Single choice dropdown | `normal`, `abandonada`, `cerrada`, `reemplazada`, `sin_calificar` |
| **Calificacion**<br>`fld16ThOYVoUuiAFF` | `number` | Numeric field |  |
| **Sugerencia**<br>`fldHO4zYmEjQ6L4Rs` | `multilineText` | Multi-line text |  |
| **EjemploExitoso**<br>`fldYU2aABG6bgqCTt` | `checkbox` | True/False checkbox |  |
| **Mensajes**<br>`fldL6s7K9zybmNuda` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **MetricasDiarias**<br>`fldyzZZIXRSOHfm8p` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **MetricasDiarias 2**<br>`fldxn7vaqpgCVhpbO` | `singleLineText` | Type: singleLineText |  |
| **SesionesEstudio**<br>`fldlinKEtBloVl1xZ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Seguimiento**<br>`fldZ5AqI2xyINL1hB` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Mensajes copy**<br>`fldG8ESeNNwzexZll` | `singleLineText` | Type: singleLineText |  |

---

## 📋 5. Curriculum

*Table ID: `tbld18R3UfqhagW4u`*
*Fields: 16*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **OA**<br>`fldrjQyvXRk6shh5j` | `multilineText` | Multi-line text |  |
| **NumeroReg**<br>`fld8fkhty8OMXYwNX` | `autoNumber` | Type: autoNumber |  |
| **OAserial**<br>`fld9wnfptnEeNincH` | `number` | Numeric field |  |
| **OAmateria**<br>`fldPPTulbJihy1UmV` | `singleSelect` | Single choice dropdown | `Matemática`, `Comprensión lectora`, `Historia y Geografía`, `Ciencias` |
| **OAeje**<br>`fldye5FSdw7sM0DGm` | `singleSelect` | Single choice dropdown | `Medición`, `Números y operaciones`, `Geometría`, `Números`, `Álgebra y funciones` *(+16 more)* |
| **OAdescripcion**<br>`fldt3pmph8IBhENoV` | `multilineText` | Multi-line text |  |
| **OAresumen**<br>`fld6bWr1pv2f0y27d` | `multilineText` | Multi-line text |  |
| **OApertinenciaContenidosM1**<br>`fld9TgFlbQzFMUPyd` | `singleSelect` | Single choice dropdown | `Alta`, `Media`, `Ausente` |
| **OApertinenciaHabilidadesM1**<br>`fldZMuh6JeacTUpSt` | `singleSelect` | Single choice dropdown | `Alta`, `Ausente`, `Media` |
| **OAtipo**<br>`fldJjHpwQVcGduK5s` | `singleSelect` | Single choice dropdown | `Basal`, `Prioritario`, `Priorización` |
| **OApertinenciaContenidosM1Respaldo**<br>`fldiPVNTu2WVLWPuR` | `multilineText` | Multi-line text |  |
| **OAhabilidades**<br>`fldRtf2rvabm7MvhR` | `singleSelect` | Single choice dropdown | `3.1. Habilidad: Resolver Problemas | 3.2. Habilidad: Modelar | 3.3. Habilidad: Representar`, `Ninguna`, `3.1. Habilidad: Resolver Problemas | 3.3. Habilidad: Representar`, `Resolver Problemas | Modelar | Representar`, `Resolver Problemas | Representar | Argumentar` *(+13 more)* |
| **OApertinenciaHabilidadesM1Respaldo**<br>`fldgk4odkACec8b56` | `multilineText` | Multi-line text |  |
| **OAnivel**<br>`fld2iZPfBxmNgBXA8` | `number` | Numeric field |  |
| **OAnivelTxt**<br>`fldqX7bbGHJFCSJb9` | `singleSelect` | Single choice dropdown | `5° Básico`, `6° Básico`, `7° Básico`, `8° Básico` |
| **OAantiguedad**<br>`fldgT3bnJbcwkUnBD` | `number` | Numeric field |  |

---

## 📋 6. EjemplosPedagogicos

*Table ID: `tblzOij9Mx124aVEy`*
*Fields: 13*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID**<br>`fld7nNpEk18RrIJ79` | `autoNumber` | Type: autoNumber |  |
| **FechaCreacion**<br>`fldkAXm3fz2N3GaQO` | `date` | Date |  |
| **TipoNEE**<br>`flddME05ykLgFBqe6` | `singleSelect` | Single choice dropdown |  |
| **Materia**<br>`fld9N4GssjTlpM6Pq` | `singleSelect` | Single choice dropdown | `Todo`, `In progress`, `Done` |
| **TemaEspecifico**<br>`fldT3xksy4ZxJqEMQ` | `singleLineText` | Type: singleLineText |  |
| **CasoEstudio**<br>`fld9upI59cIpKYtM4` | `singleLineText` | Type: singleLineText |  |
| **PromptUtilizado**<br>`fld8i2Cspjx7N8m3e` | `multilineText` | Multi-line text |  |
| **InteraccionEstudiante**<br>`fldpMrypMehg5i8Sh` | `multilineText` | Multi-line text |  |
| **RespuestaAsistente**<br>`fldBA0VCTRRxL02Ld` | `multilineText` | Multi-line text |  |
| **Resultado**<br>`fldYS38LT3pnbbC7x` | `singleSelect` | Single choice dropdown | `éxito`, `mejorable`, `fallo` |
| **Aprendizaje**<br>`flddqjxmk7pntxYyx` | `multilineText` | Multi-line text |  |
| **TuRating**<br>`fld0aNINPo9rJ1cul` | `number` | Numeric field |  |
| **Tags**<br>`fldp9aZ3JJjHYL0mC` | `multipleSelects` | Multiple choice dropdown | `timer`, `refuerzo_positivo`, `instrucciones_cortas` |

---

## 📋 7. Estudiantes

*Table ID: `tblR5gbkydy59GOOC`*
*Fields: 115*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Estudiante**<br>`fldp7qIUatWYG2zw2` | `autoNumber` | Type: autoNumber |  |
| **Email**<br>`fldaPohMI9tlgDW4t` | `email` | Email address |  |
| **IDExternoPago**<br>`fld6P8XQEE3SNZy7X` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **SesionActivaToken**<br>`fldeNdxf94vhx95qp` | `singleLineText` | Type: singleLineText |  |
| **SesionActivaDeviceId**<br>`fld8hno4n2Q0byffc` | `singleLineText` | Type: singleLineText |  |
| **Contrasena**<br>`fld2VACy7rMKduyLP` | `multilineText` | Multi-line text |  |
| **Rol**<br>`fld62uCAFaxkz5scC` | `singleSelect` | Single choice dropdown | `Estudiante`, `Apoderado`, `Admin` |
| **Nombre**<br>`fldDs68JQokh38DX6` | `singleLineText` | Type: singleLineText |  |
| **PlanActual**<br>`fldnLcg9DbxjdWCN2` | `singleLineText` | Type: singleLineText |  |
| **FechaVencimientoPlan**<br>`fldleXvHmd3Xg9pSJ` | `date` | Date |  |
| **FechaEliminacion**<br>`fldYNz9WZM6kirtaG` | `date` | Date |  |
| **ModalidadPremium**<br>`fldyFxnLf3QYEoYKj` | `singleSelect` | Single choice dropdown | `Pago_Normal`, `Pago_Campaña`, `Descuento_Grupal`, `Beca_Colegio`, `Beca_Personal` *(+1 more)* |
| **CampanaId**<br>`fldwWox9y7hTiykir` | `singleLineText` | Type: singleLineText |  |
| **TramoGrupal**<br>`fldqdmmP5SqdO9ex8` | `singleSelect` | Single choice dropdown | `T1`, `T2`, `T3` |
| **PrecioPagadoMensual**<br>`fldQacjN5GCulioWn` | `number` | Numeric field |  |
| **Moneda**<br>`fldITHTQ5KLfx96Ax` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaPago**<br>`fldUL833KTrU6As0a` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaProximoVencimiento**<br>`fldv97mLTiSL3s5yj` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **LlegoPor**<br>`fld51E4NaVZvq9upz` | `singleSelect` | Single choice dropdown | `ChatGPT u otra IA`, `Convenio con tu colegio`, `Dato o consejo de un(a) amigo(a)`, `Facebook`, `Google` *(+5 more)* |
| **QuienDecidio**<br>`fldocqWgnEkChM2nQ` | `singleSelect` | Single choice dropdown | `Yo`, `Mi padre-madre o tutor(a)` |
| **Genero**<br>`fldQ7uWbpXHadpSMA` | `singleSelect` | Single choice dropdown | `Hombre`, `Mujer`, `Otro`, `Prefiero no registrarlo` |
| **Estado**<br>`fldN9UGcBbKrtGPYD` | `singleSelect` | Single choice dropdown | `Activo`, `Bloqueado`, `suspendido` |
| **Pais**<br>`fldlqQYUn3GMAVXHW` | `formula` | Calculated field | Formula: `IF({fld4e4pFqnpODVbJB}="",
  SWITCH({fldl1SW9SPvQ...` |
| **PaisElegido**<br>`fld4e4pFqnpODVbJB` | `singleSelect` | Single choice dropdown | `Chile`, `Argentina`, `Perú`, `Colombia`, `México` *(+7 more)* |
| **TZ**<br>`fldBKjR4g8qcF9JZV` | `formula` | Calculated field | Formula: `IF({fld4e4pFqnpODVbJB}!="",
  SWITCH(
    {fld4e...` |
| **CodigoPais**<br>`fldl1SW9SPvQcxIpY` | `formula` | Calculated field | Formula: `IF({fld4e4pFqnpODVbJB}!="",
  SWITCH({fld4e4pFqnp...` |
| **Celular**<br>`fldDJTv1TC3Dwr8b1` | `phoneNumber` | Phone number |  |
| **NombrePreferido**<br>`fldLdC48e8cV7Qn1f` | `singleLineText` | Type: singleLineText |  |
| **Curso**<br>`fldhlrRfO42asiEru` | `singleSelect` | Single choice dropdown | `7 Básico`, `8 Básico`, `1 Medio`, `2 Medio`, `3 Medio` *(+1 more)* |
| **FechaNacimiento**<br>`fldBHYunaLfzhfzNN` | `date` | Date |  |
| **EdadActual**<br>`fldqWWnlGSugEUugs` | `number` | Numeric field |  |
| **EstiloAprendizaje**<br>`fld0ckIVlh46CtbVb` | `singleSelect` | Single choice dropdown | `Visual`, `Auditivo`, `Kinestésico`, `Lectura/Escritura`, `No lo sé` |
| **MateriasFuertes**<br>`fldNhz8Feiohchzi1` | `singleSelect` | Single choice dropdown | `Matemáticas`, `Lenguaje`, `Ciencias`, `Historia` |
| **MateriasDebiles**<br>`fldH2m6C9msfoYLRn` | `singleSelect` | Single choice dropdown | `Lenguaje`, `Historia`, `Matemáticas`, `Ciencias` |
| **HaRepetido**<br>`fldZgc8D6koiQgda4` | `checkbox` | True/False checkbox |  |
| **TiposNEE**<br>`fld4uN4bHlLVEz3Mx` | `multipleSelects` | Multiple choice dropdown | `TDAH`, `Dislexia`, `TEA`, `Discalculia`, `Ninguno` *(+1 more)* |
| **RecibePIE**<br>`fldn3Sioto5nfisur` | `checkbox` | True/False checkbox |  |
| **NivelAnsiedad**<br>`fld5u3seaJi0JePIG` | `number` | Numeric field |  |
| **InteresesPersonales**<br>`fldykiNRSZPdeVHw6` | `multipleSelects` | Multiple choice dropdown | `Practicar deportes`, `Videojuegos en consola`, `Escuchar música`, `Leer`, `Pasear en la Naturaleza` *(+8 more)* |
| **Idolo**<br>`fldlI8eMEZJCzBo7Y` | `singleLineText` | Type: singleLineText |  |
| **AspiracionFutura**<br>`fldlS5kKiRrjMMLuo` | `multilineText` | Multi-line text |  |
| **OnboardingCompletado**<br>`fld1peJxyAKgqLRg6` | `checkbox` | True/False checkbox |  |
| **FechaRegistro**<br>`fldvMB0YXrUFGNThv` | `dateTime` | Date and time |  |
| **UltimaActividad**<br>`fld00gaBZOkktKJYO` | `dateTime` | Date and time |  |
| **DiasDesdeUltima**<br>`fldYd2NI4ued8FXc7` | `formula` | Calculated field | Formula: `DATETIME_DIFF(
     SET_TIMEZONE(NOW(), 'America/...` |
| **CantidadConversacionesDeDias**<br>`fldkF1lllYaBcR4Bl` | `formula` | Calculated field | Formula: `{fldJZJ0PotO13gABR}+{fldA3hx5Y8HUCQQxe}+{fldT3F5dU...` |
| **CantidadConversacionesExitosas**<br>`fldY1vwqXfZLzzn2W` | `count` | Type: count |  |
| **CantidadConversacionesTotales**<br>`fld3EuETc0w2ZsgZr` | `count` | Type: count |  |
| **Lunes**<br>`fldJZJ0PotO13gABR` | `count` | Type: count |  |
| **Martes**<br>`fldA3hx5Y8HUCQQxe` | `count` | Type: count |  |
| **Miercoles**<br>`fldT3F5dUstvcWDaK` | `count` | Type: count |  |
| **Jueves**<br>`fld4HMaw3xuTrYZU5` | `count` | Type: count |  |
| **Viernes**<br>`fldmNChD1n8TMgyn6` | `count` | Type: count |  |
| **Sabado**<br>`fldYKlDDHfaK3G3ef` | `count` | Type: count |  |
| **Domingo**<br>`fldaEGcdWiDRYl7Nc` | `count` | Type: count |  |
| **Suscripciones**<br>`fldUJgVD2lFOWBZg4` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pagador**<br>`fldknWUUzzBo3RZ4h` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **EmailPagador**<br>`fldA4uOWRPNo3IR0f` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **EstadoCuentaPagador**<br>`fldZbyD2Nc89fK4MN` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Conversaciones**<br>`fldkSWz9udhZOD1pZ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Brechas**<br>`fldGzudn4tRsgmydF` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Planes**<br>`fldKW0KGyhpogBEM9` | `singleLineText` | Type: singleLineText |  |
| **Logros**<br>`fldjGdoFj8YyOa6BK` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Recordatorios**<br>`fldUT4s4hWISFhvN0` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EventosSignificativos**<br>`fldwNGfi1Trbu6gXi` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **recordId**<br>`fldzO8FoTnfACQMpG` | `formula` | Calculated field | Formula: `RECORD_ID()` |
| **MetricasDiarias**<br>`fldVuv0xoETAWTGIZ` | `singleLineText` | Type: singleLineText |  |
| **Pagos**<br>`fldX2wJ29vjy4LcNL` | `singleLineText` | Type: singleLineText |  |
| **Suscripciones 2**<br>`fldCu7SFplfevjAgA` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pagadores**<br>`fldH7DEBRiJeWrWQO` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pagos 2**<br>`fldJnzfYBW5XHQxU8` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **TokenReset**<br>`fldObhyfttEMNyDuu` | `multilineText` | Multi-line text |  |
| **ExpiraReset**<br>`fldM7GFnh4adVSyx2` | `dateTime` | Date and time |  |
| **DesafiosEspecificos**<br>`fld17Q7JtuZbAIATf` | `multipleSelects` | Multiple choice dropdown | `Atención sostenida`, `Memoria de trabajo`, `Decodificación lectora`, `Comprensión de textos`, `Inicio de tareas` *(+8 more)* |
| **FortalezasCognitivas**<br>`fld5lyEpWQDVoOHn1` | `multipleSelects` | Multiple choice dropdown | `Visual-espacial`, `Verbal-lingüística`, `Corporal-kinestésica`, `Lógico-matemática`, `Interpersonal` *(+2 more)* |
| **PerfilExplicado**<br>`fld1EPlFr6rlyET2K` | `checkbox` | True/False checkbox |  |
| **EtapaDiagnostico**<br>`fldXdivQkcqxOU371` | `singleSelect` | Single choice dropdown | `sin_iniciar`, `fortalezas_detectadas`, `desafios_detectados`, `completo` |
| **PreferenciaSensorial**<br>`fldsv5r1F9fSTfeqh` | `singleSelect` | Single choice dropdown | `Visual`, `Auditivo`, `Kinestésico`, `Lectura-escritura`, `Mixto` |
| **InteresesProfundos**<br>`fldWLNcnsUgrGa8fW` | `multilineText` | Multi-line text |  |
| **TecnicaExitosa**<br>`fldSvEUCMpOi9wTgw` | `singleSelect` | Single choice dropdown | `Cornell`, `Feynman`, `MapasMentales`, `RepeticionEspaciada`, `Autoexplicacion` *(+2 more)* |
| **GestionTiempoPreferida**<br>`fld5wX8Q0Mg2K8y6E` | `singleSelect` | Single choice dropdown | `Pomodoro-15`, `Pomodoro-25`, `Pomodoro-50`, `Bloques-tematicos`, `Libre` *(+1 more)* |
| **SesionesEstudio**<br>`fldtXmk3sda4E269Q` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Seguimiento**<br>`fldwkiUb2xuYkjoKj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Push_Subscription**<br>`fldiRXDQpOjg4uR6c` | `multilineText` | Multi-line text |  |
| **Notificaciones_Activas**<br>`fldp8a9rl5JwiJIEr` | `checkbox` | True/False checkbox |  |
| **SSO_Provider**<br>`fld3rYzqN4VUtw4Bj` | `singleSelect` | Single choice dropdown | `google`, `apple`, `email`, `legacy` |
| **SSO_ProviderID**<br>`fld1bIxqwZIlOELiw` | `singleLineText` | Type: singleLineText |  |
| **LoginMethod**<br>`fldzkXML6QwcEy2rg` | `singleSelect` | Single choice dropdown | `email`, `google`, `apple` |
| **FotoPerfil**<br>`fldZfFUfmilD7lkGj` | `url` | URL link |  |
| **ConsentimientoPrivacidad**<br>`fldf0McnfLC7GHfNe` | `checkbox` | True/False checkbox |  |
| **ConsentimientoTerminos**<br>`fldDuwcqXoNWxa2Sf` | `checkbox` | True/False checkbox |  |
| **FechaConsentimiento**<br>`fldCXlCEXEPSXnOso` | `dateTime` | Date and time |  |
| **VersionConsentimientoPrivacidad**<br>`fldW806HTDiGPOuTb` | `singleLineText` | Type: singleLineText |  |
| **VersionConsentimientoTerminos**<br>`fldafyDVp3nlKaTAS` | `singleLineText` | Type: singleLineText |  |
| **EmailVerificado**<br>`fldrDwPxquu2KGEY1` | `checkbox` | True/False checkbox |  |
| **RequiereConsentimientoParental**<br>`fldlBYsfa4cYGWKWU` | `checkbox` | True/False checkbox |  |
| **EstadoConsentimientoParental**<br>`fldGQiCgFthYb2hdv` | `singleSelect` | Single choice dropdown | `no_requerido`, `pendiente`, `otorgado`, `revocado` |
| **TokenAutorizacionParental**<br>`fld0OkdR69ANOfzWh` | `singleLineText` | Type: singleLineText |  |
| **TokenExpiracion**<br>`fldRk7px6Zoj0Fm87` | `dateTime` | Date and time |  |
| **ConsentidorNombre**<br>`fld0IGWNXeXxAfW7L` | `singleLineText` | Type: singleLineText |  |
| **ConsentidorRelacion**<br>`fldKCEPepa3HTkRNK` | `singleSelect` | Single choice dropdown | `Padre`, `Madre`, `Tutor Legal` |
| **ConsentidorEmail**<br>`fldAVfMKqn7bY8OOJ` | `email` | Email address |  |
| **FechaConsentimientoParental**<br>`fld2x2CfKdTKUaBBO` | `dateTime` | Date and time |  |
| **ConsentidorIP**<br>`fldMo2OBRZxpqDnGl` | `singleLineText` | Type: singleLineText |  |
| **ConsentidorUserAgent**<br>`fldwPadlV8LGmmfLI` | `singleLineText` | Type: singleLineText |  |
| **IPRegistro**<br>`fldtdS5JrOWCHtC3R` | `singleLineText` | Type: singleLineText |  |
| **PaisDetectadoIP**<br>`fldeSwPyE7ua5wtSb` | `singleLineText` | Type: singleLineText |  |
| **AlertaPais**<br>`fld6eEMgawAjwleQp` | `formula` | Calculated field | Formula: `IF({fldl1SW9SPvQcxIpY}!={fldeSwPyE7ua5wtSb},"!","O...` |
| **ConfirmaEdad**<br>`flduUy3LxXTKr9SFw` | `checkbox` | True/False checkbox |  |
| **FechaConfirmaEdad**<br>`fldfeZ0wWjVxQFR5C` | `dateTime` | Date and time |  |
| **Anuncios**<br>`fldnbVzJLcx4NsUuj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AnunciosVistos**<br>`fld3I3aEDwtqgz2W9` | `singleLineText` | Type: singleLineText |  |
| **Testimonios**<br>`fldx7wYmuAkcXwfPA` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **PlanRiesgo**<br>`fldafI2tXD93EhK4j` | `checkbox` | True/False checkbox |  |
| **AvatarURL**<br>`fld9NmFP2vnePNzyj` | `url` | URL link |  |

---

## 📋 8. EventosSignificativos

*Table ID: `tblKU5sD9MdcTQmSH`*
*Fields: 8*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID**<br>`fldlMD8qLO1qMbn3j` | `autoNumber` | Type: autoNumber |  |
| **Timestamp**<br>`fldGK0v40C91xCkQD` | `dateTime` | Date and time |  |
| **Usuario**<br>`fld2OiSMOXDN3dUGT` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **TipoEvento**<br>`fldH058ArfLzCuoEy` | `singleSelect` | Single choice dropdown | `primera_sesion`, `resolucion_exitosa`, `sesion_larga_5min`, `uso_imagen`, `cambio_materia` *(+2 more)* |
| **Materia**<br>`fldZf4OThGc5JU7y5` | `singleLineText` | Type: singleLineText |  |
| **TipoNEE**<br>`fldI6weNWvtgebLy6` | `singleLineText` | Type: singleLineText |  |
| **TiempoHastaEvento**<br>`fldDjBVVgPRp2KaMO` | `number` | Numeric field |  |
| **DatosContexto**<br>`fld7wFo3pRTystgMN` | `multilineText` | Multi-line text |  |

---

## 📋 9. Logros

*Table ID: `tblIezwTdqN8x1T8H`*
*Fields: 6*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Logro**<br>`fldAwA7SnR5HTm03i` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldBzozokHjNTta8A` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **TipoLogro**<br>`fldhM2BYZ0XfIkM6H` | `singleSelect` | Single choice dropdown | `🎯 Brecha`, `✅ Plan`, `💡 Técnica`, `🏆 Desafío` |
| **Descripcion**<br>`fldLBM5BR5yMMb1gS` | `multilineText` | Multi-line text |  |
| **Celebrado**<br>`fldmEG2JSPOy24TP9` | `checkbox` | True/False checkbox |  |
| **FechaLogro**<br>`fldeISuhbfRFcF7O1` | `createdTime` | Auto-generated creation time |  |

---

## 📋 10. Mensajes

*Table ID: `tblk3NUMOZhQX42AJ`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Mensaje**<br>`fldICiv65DcYl0ZMO` | `autoNumber` | Type: autoNumber |  |
| **Conversacion**<br>`fld0lhvJqLpoX8lzh` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiante**<br>`fldq4HaCjf56NmdNv` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Rol**<br>`fldrBWwu17uehpmwN` | `singleSelect` | Single choice dropdown | `estudiante`, `asistente`, `sistema` |
| **Contenido**<br>`fldskyjOSEa80QeoI` | `richText` | Rich text with formatting |  |
| **TokensCacheados**<br>`fldpIXq8JPF2CFEhG` | `number` | Numeric field |  |
| **TokensInput**<br>`fldRT5Mct3fm4KNdS` | `number` | Numeric field |  |
| **TokensOutput**<br>`fld2ssxNptWy6YTJ9` | `number` | Numeric field |  |
| **TokensUsados**<br>`fld7kXyt2mxu2jff8` | `number` | Numeric field |  |
| **ModeloIA**<br>`fld0hzK2Pf0nah5Uq` | `singleLineText` | Type: singleLineText |  |
| **Timestamp**<br>`fldrycW7y7bBFaLUy` | `createdTime` | Auto-generated creation time |  |
| **ContieneImagen**<br>`fld8ohAvc4OTu8d7K` | `checkbox` | True/False checkbox |  |
| **MetricasDiarias**<br>`fldPbYZ1ceJdydjrN` | `singleLineText` | Type: singleLineText |  |
| **CostoMensaje**<br>`fldSYiKZmNSUahvGN` | `number` | Numeric field |  |

---

## 📋 11. MetricasDiarias

*Table ID: `tblgF1aCbdkC8PWU7`*
*Fields: 16*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID**<br>`fldHDPrDh8gb6fR7h` | `autoNumber` | Type: autoNumber |  |
| **Fecha**<br>`fldYyiouH6h96oy1W` | `date` | Date |  |
| **UsuariosActivos**<br>`fld5Zj8l5ASpHH6o4` | `number` | Numeric field |  |
| **UsuariosNuevos**<br>`fldUaM9EiUzsZcwYc` | `number` | Numeric field |  |
| **ConversacionesDeHoy**<br>`fldC2o4is6XRs2b6s` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **SesionesTotales**<br>`fldX5SL4C2Gvstv7g` | `number` | Numeric field |  |
| **MensajesProcesados**<br>`fldeIoHc6Mml15O5G` | `number` | Numeric field |  |
| **ImagenesProcesadas**<br>`fld26wuwmv5ZMVzcL` | `number` | Numeric field |  |
| **TiempoSesionPromedio**<br>`fldjD3VhufVlCgx94` | `number` | Numeric field |  |
| **MateriaPrincipal**<br>`fldqJSZzHM6qSXs6v` | `singleLineText` | Type: singleLineText |  |
| **EjemplosExitosos**<br>`fldP735LNZKJO3vD0` | `number` | Numeric field |  |
| **Errores**<br>`fldoI5Qex28nI3Tq5` | `number` | Numeric field |  |
| **CostoEstimado	**<br>`fldJjSPpuvmsEmOmP` | `currency` | Currency amount |  |
| **CostoReal**<br>`fldmpV5gSeK0BejGh` | `number` | Numeric field |  |
| **TokensCacheados**<br>`fldBOfD4GHEDf9CE1` | `number` | Numeric field |  |
| **PctCacheHit**<br>`fldIW4dbH7Sds76fN` | `number` | Numeric field |  |

---

## 📋 12. MetricasNEE

*Table ID: `tblZ8HxhJrrePHPNE`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID**<br>`fldq6vOiPmnNN7K0O` | `autoNumber` | Type: autoNumber |  |
| **Fecha**<br>`fldH1YL9fkoLNgrUt` | `date` | Date |  |
| **TipoNEE**<br>`fldGv8zGpyrkVjgsw` | `singleLineText` | Type: singleLineText |  |
| **UsuariosActivos**<br>`fldOsZv0DOZ1ozZhB` | `number` | Numeric field |  |
| **SesionesTotales**<br>`fldGyy8JagN79lo0N` | `number` | Numeric field |  |
| **TasaResolucion**<br>`fldTqsR29L5vj9mjp` | `percent` | Percentage |  |
| **TiempoSesionPromedio**<br>`fld26JiW2t2Xj8q2B` | `number` | Numeric field |  |
| **UsoImagenesPorcentaje**<br>`fldrXqInkbPBIxf8G` | `percent` | Percentage |  |
| **TasaAbandono**<br>`fldNCeRR4Wmj0Dd3G` | `percent` | Percentage |  |
| **SatisfaccionEstimada**<br>`fldF8Nzm8gmYd66LQ` | `number` | Numeric field |  |

---

## 📋 13. Pagadores

*Table ID: `tblkl6i81e7fyKRKI`*
*Fields: 18*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Pagador**<br>`fldg8kZfm23qJl5xy` | `autoNumber` | Type: autoNumber |  |
| **EmailPagador**<br>`fld1Q9CSkUF77j9LP` | `email` | Email address |  |
| **NombrePagador**<br>`fldkL3EyqzWW1wL4M` | `singleLineText` | Type: singleLineText |  |
| **Pais**<br>`fldQbrxB2cSmt5f9R` | `singleSelect` | Single choice dropdown | `Chile`, `Argentina`, `Colombia`, `Perú` |
| **Telefono**<br>`fldQhK77UwmvslBrZ` | `phoneNumber` | Phone number |  |
| **MetodoPagoPreferido**<br>`fldokDvkhzblTnMdP` | `singleSelect` | Single choice dropdown | `Paddle`, `MercadoPago` |
| **PaddleCustomerId**<br>`fld5pSHg2tbdnLIqU` | `singleLineText` | Type: singleLineText |  |
| **EstadoCuentaPagador**<br>`fld8np85ERgOfAavC` | `singleSelect` | Single choice dropdown | `Freemium`, `Premium`, `Suspendido` |
| **UltimoPago**<br>`fldsX9Bz2og25BoJE` | `date` | Date |  |
| **ProximoPago**<br>`fldciVzK93W0RtcPQ` | `date` | Date |  |
| **Estudiantes**<br>`fldupV0UVJjyyGduY` | `singleLineText` | Type: singleLineText |  |
| **EstudiantesLink**<br>`fldmjLB3KCHZvp7HF` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Suscripciones 2**<br>`fld22Uw0FjNQpnp6T` | `singleLineText` | Type: singleLineText |  |
| **Suscripciones 2 copy**<br>`fldKZHlloJfYuHr6C` | `singleLineText` | Type: singleLineText |  |
| **Pagos 2**<br>`fld8aiJlfvcRFqjx7` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiantes 2**<br>`fldVeygK325XpCUGs` | `singleLineText` | Type: singleLineText |  |
| **Suscripciones**<br>`fld7g9e3zB5R9TalE` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Suscripciones copy**<br>`fldzOJM80DzvoN1hy` | `singleLineText` | Type: singleLineText |  |

---

## 📋 14. Pagos

*Table ID: `tbllGZKmZYWmRTZk1`*
*Fields: 17*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Pago**<br>`fldtamvOsSzchyolz` | `singleLineText` | Type: singleLineText |  |
| **Suscripcion**<br>`fldzQgXVKQJKfEAdg` | `singleLineText` | Type: singleLineText |  |
| **SuscripcionLink**<br>`fldteh6mV1X0mOcJR` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiante (from SuscripcionLink)**<br>`fldFaoQYcPlHERRe9` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Pagador (from SuscripcionLink)**<br>`fldsXeO0t23vTh2n7` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Pagador**<br>`fldBLCDiPmIcG2yOF` | `singleLineText` | Type: singleLineText |  |
| **PagadorLink**<br>`fldre47MsdNJIm0VX` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EmailPagador**<br>`fldCUm6EX5urKIZF1` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Estudiante**<br>`fldk2QtZa6qC3nqan` | `singleLineText` | Type: singleLineText |  |
| **EstudianteLink**<br>`fldHkWqqbUKm2LZSB` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EstadoPago**<br>`fldXORkBWE7Czx24V` | `singleSelect` | Single choice dropdown | `Exitoso`, `Fallido`, `Reembolsado` |
| **FechaPago**<br>`fldFLBDQ3aU8rUCFG` | `date` | Date |  |
| **Monto**<br>`fldxTsBDMUAOlNLeI` | `number` | Numeric field |  |
| **Moneda**<br>`fldGcDvLW4rImhuMU` | `singleLineText` | Type: singleLineText |  |
| **OrigenWebhook**<br>`fld1tGdy1Qrt9XHlG` | `singleLineText` | Type: singleLineText |  |
| **RawPayload**<br>`fldfgKOo7FbphW8FE` | `multilineText` | Multi-line text |  |
| **Suscripciones**<br>`fldj6NcyLD82RUqEU` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 15. ParametrosGenerales

*Table ID: `tblGybdcCD0zm1STD`*
*Fields: 5*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Clave**<br>`fldMsdbRVzIYcl2wq` | `singleLineText` | Type: singleLineText |  |
| **Valor**<br>`fld1fmU98qlLL9YSw` | `singleLineText` | Type: singleLineText |  |
| **Descripcion**<br>`fld5xp1JDPsHpmVYl` | `singleLineText` | Type: singleLineText |  |
| **Ambiente**<br>`fld8uCIwpwnfjrrNI` | `singleSelect` | Single choice dropdown | `PROD`, `DEV`, `AMBOS` |
| **UltimaModificacion**<br>`fld2wiyQaLcIbd62x` | `lastModifiedTime` | Auto-generated modification time |  |

---

## 📋 16. PlanesEstudio

*Table ID: `tblQbkeIjxnW6GZnI`*
*Fields: 11*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Plan**<br>`fldTq0FghQ6k2GAJX` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldNW8O6Jz0lHdwTp` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estado**<br>`fld54jlYyQKdL0uKt` | `singleSelect` | Single choice dropdown | `activo`, `pausado`, `completado`, `abandonado` |
| **FechaInicio**<br>`fldvyfotUMZfeaz41` | `createdTime` | Auto-generated creation time |  |
| **FechaFin**<br>`fldE5SwVi3KvEBFqB` | `date` | Date |  |
| **DiagnosticoInicial**<br>`fldMuHk8pRiZDsV02` | `multilineText` | Multi-line text |  |
| **TecnicaAsignada**<br>`fldUaxtqVORS1HKin` | `singleSelect` | Single choice dropdown | `Cornell`, `Feynman`, `MapasMentales`, `RepeticionEspaciada`, `Autoexplicacion` *(+1 more)* |
| **GestionTiempoAsignada**<br>`fldJjIYhOVfEqs92m` | `singleSelect` | Single choice dropdown | `Pomodoro-15`, `Pomodoro-25`, `Pomodoro-50`, `Bloques-tematicos`, `Libre` |
| **TiempoSemanalComprometido**<br>`fld8n12MEjh7RnXna` | `number` | Numeric field |  |
| **Notas**<br>`fldbnImFOu5l6zDLj` | `multilineText` | Multi-line text |  |
| **SesionesEstudio**<br>`fldC4qecCVPvtXQiM` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 17. PostulacionesConvenios

*Table ID: `tblU7CHwVifHvTYDF`*
*Fields: 16*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Rec**<br>`fldPYxxRrEPcH5185` | `autoNumber` | Type: autoNumber |  |
| **FechaIngreso**<br>`flddVMlA67KB0y9I8` | `createdTime` | Auto-generated creation time |  |
| **Pais**<br>`fld60qkbLxX00uKWK` | `singleSelect` | Single choice dropdown |  |
| **EstadoProvincia**<br>`fldqKNgEe80ISS5vd` | `singleSelect` | Single choice dropdown | `Todo`, `In progress`, `Done` |
| **Ciudad**<br>`fldVJ4oFappSSVewR` | `singleSelect` | Single choice dropdown |  |
| **Colegio**<br>`fldmzJCnbzRviRVlH` | `singleLineText` | Type: singleLineText |  |
| **Dependencia**<br>`fldaJB3ozQXRwXkFH` | `singleSelect` | Single choice dropdown |  |
| **MatriculaTotal**<br>`fld3zQbi9ZodLIcvS` | `number` | Numeric field |  |
| **NombreSolicitante**<br>`fldE2eq4PDyUX2GHr` | `singleLineText` | Type: singleLineText |  |
| **CargoSolicitante**<br>`fldtuuFGUeKVMvDfc` | `singleLineText` | Type: singleLineText |  |
| **EmailSolicitante**<br>`fld8xURPPDngG9MYC` | `email` | Email address |  |
| **TelefonoSolicitante**<br>`fldA8kJNZyhq7Jvyq` | `phoneNumber` | Phone number |  |
| **RevisadaAutomatica**<br>`fld3GpaRUchUlpchb` | `dateTime` | Date and time |  |
| **RevisadaManual**<br>`flduaQA892j5ek4t9` | `dateTime` | Date and time |  |
| **Aprobada**<br>`fldY4FuyGQIneX8oM` | `checkbox` | True/False checkbox |  |
| **MotivoRechazo**<br>`fldmp9E5z1K5ao4Aj` | `multilineText` | Multi-line text |  |

---

## 📋 18. Recordatorios

*Table ID: `tbll95VSiGdzEPEsZ`*
*Fields: 7*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Recordatorio**<br>`fldCeJs9p3YhILtkp` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`flds4OsLlxdLog8Vl` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Tipo**<br>`fld7GBBxkFKT87KRP` | `singleSelect` | Single choice dropdown | `Plan`, `Coaching`, `Revisar` |
| **Mensaje**<br>`fldegBwIzQ4jge8hl` | `multilineText` | Multi-line text |  |
| **FechaHora**<br>`fldNmVKZlf4pLpTfH` | `dateTime` | Date and time |  |
| **Enviado**<br>`fldm1HxklxmQ8BWKR` | `checkbox` | True/False checkbox |  |
| **FechaCreacion**<br>`fldqaefpAMBXwIHYU` | `createdTime` | Auto-generated creation time |  |

---

## 📋 19. RecursosDidacticos

*Table ID: `tblhnDhyfno9kEmFd`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Recurso**<br>`fldZaD23G5fA1oFM4` | `autoNumber` | Type: autoNumber |  |
| **Nombre**<br>`fldOTouTbrUpVbVzU` | `singleLineText` | Type: singleLineText |  |
| **Tipo**<br>`fld8xRCJ1LFqYQEgc` | `singleSelect` | Single choice dropdown | `Técnica`, `GestionTiempo`, `Otro` |
| **Categoria**<br>`fld51T1Ay8nHSKoxs` | `singleSelect` | Single choice dropdown | `Feynman`, `Cornell`, `MapasMentales`, `Pomodoro-15`, `Pomodoro-25` *(+1 more)* |
| **URL_Video**<br>`fldnMmWVkFixZi0PL` | `url` | URL link |  |
| **URL_Articulo**<br>`fld6jOLm5FckN8E6L` | `url` | URL link |  |
| **DescripcionCorta**<br>`fldciO6vLftnABiqJ` | `multilineText` | Multi-line text |  |
| **PasosResumidos**<br>`fldEWU6tdsS5PwyLI` | `multilineText` | Multi-line text |  |
| **DiagramaASCII**<br>`fldZKFwCfFIrYtNvs` | `multilineText` | Multi-line text |  |
| **IdealPara**<br>`fldBZATWF6Wd94WM4` | `multipleSelects` | Multiple choice dropdown | `TDAH`, `TEA`, `Dislexia`, `Visual`, `Verbal` *(+1 more)* |
| **IdiomaHablado**<br>`fldL00xPEjB8ZMVh3` | `singleSelect` | Single choice dropdown | `Español`, `Inglés` |
| **IdiomaSubtitulos**<br>`fldeftShiOyc4dtyP` | `singleSelect` | Single choice dropdown | `Español`, `Inglés` |
| **Observaciones**<br>`fldDq4XrcYNJ3mKqj` | `singleLineText` | Type: singleLineText |  |
| **Activo**<br>`fldJRQTRII9zoVDHC` | `checkbox` | True/False checkbox |  |

---

## 📋 20. Seguimiento

*Table ID: `tblq2wnV8lPEHKb8p`*
*Fields: 21*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Seguimiento**<br>`fldE4SpsvkoA2kGIp` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldYq22cPBj5DIGFA` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Email_Estudiante**<br>`fldpf9LPldEfOEAhz` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Nombre_Estudiante**<br>`fldNxDZT5Y1C9fKRj` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **NEE_Estudiante**<br>`fldJ8nt1DhqzK86iA` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Puerta**<br>`fldRE5Kx3rJfj6mDe` | `singleSelect` | Single choice dropdown | `aprender`, `estudiar`, `preparar-evaluacion`, `mejorar-habitos` |
| **Contexto_Especifico**<br>`fldlBRLW13BwtXmib` | `multilineText` | Multi-line text |  |
| **Estado**<br>`fldcZL43YOKNRg5o0` | `singleSelect` | Single choice dropdown | `activo`, `pausado`, `completado`, `abandonado` |
| **Fase_Actual**<br>`fldsDHIIuiVfmnG2u` | `multilineText` | Multi-line text |  |
| **Numero_Sesion**<br>`fldptShMJhlnse1Eo` | `number` | Numeric field |  |
| **Fecha_Inicio**<br>`fld7dFPef4NPf8h5x` | `createdTime` | Auto-generated creation time |  |
| **Ultima_Actualizacion**<br>`flddJlsYkR1dpudly` | `lastModifiedTime` | Auto-generated modification time |  |
| **Dias_Desde_Ultima**<br>`flde7eZE7OovOVocD` | `formula` | Calculated field | Formula: `DATETIME_DIFF(
     SET_TIMEZONE(NOW(), 'America/...` |
| **Fecha_Proximo_Checkin**<br>`fldYcCzIiOqQcFole` | `date` | Date |  |
| **Resumen_Progreso**<br>`fldZSGkLa7laEIrVH` | `multilineText` | Multi-line text |  |
| **Resultados_Reportados**<br>`fldyd9iCs4YOxkXnM` | `multilineText` | Multi-line text |  |
| **Desafios_Pendientes**<br>`fld23eS2PpyPc5IMy` | `multilineText` | Multi-line text |  |
| **Estrategia_Actual**<br>`fldLmnovnSMgh75wN` | `multilineText` | Multi-line text |  |
| **Proxima_Accion**<br>`fldZFq6mxXqfkI6Su` | `multilineText` | Multi-line text |  |
| **Reactivacion_Enviada**<br>`fldAfpeDIt3cp0FQU` | `checkbox` | True/False checkbox |  |
| **Link_Conversacion**<br>`fldt6cIweSGmQBHnz` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 21. SesionesEstudio

*Table ID: `tbliVHFlDjE2UlO5c`*
*Fields: 16*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Sesion**<br>`fldZvelM7SvT5Zftn` | `autoNumber` | Type: autoNumber |  |
| **Plan**<br>`fld8YRNnApHWFff7j` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **NumeroSesion**<br>`fld1Zg53OxGh0HvoI` | `number` | Numeric field |  |
| **FechaSesion**<br>`fldmummD5rHmkMths` | `createdTime` | Auto-generated creation time |  |
| **EstadoSesion**<br>`fld6NW7fBhTVB2uIP` | `singleSelect` | Single choice dropdown | `en_curso`, `completada`, `abandonada`, `sin_confirmar` |
| **TecnicaUsada**<br>`fld3zaaMogD73rN0x` | `singleSelect` | Single choice dropdown | `Cornell`, `Feynman`, `MapasMentales`, `RepeticionEspaciada`, `Autoexplicacion` *(+1 more)* |
| **GestionUsada**<br>`fld8qiAqV1SyZOq7w` | `singleSelect` | Single choice dropdown | `Pomodoro-15`, `Pomodoro-25`, `Pomodoro-50`, `Bloques-tematicos`, `Libre` |
| **MateriaEstudiada**<br>`fldIjZNiF3Y2lPSrx` | `singleSelect` | Single choice dropdown | `Matemáticas`, `Lenguaje`, `Ciencias`, `Historia`, `Inglés` *(+4 more)* |
| **TemaEspecifico**<br>`fldeLSd9sBtn1hVmQ` | `singleLineText` | Type: singleLineText |  |
| **DuracionMinutos**<br>`fldYdyKpYhAaMD2DB` | `number` | Numeric field |  |
| **BloquesCompletados**<br>`fldwTIvLGt4eKV8SU` | `number` | Numeric field |  |
| **EvaluacionMetodo**<br>`fldvCVGRsMdhzw17A` | `number` | Numeric field |  |
| **EvaluacionProductividad**<br>`fldtgbHVPf6cU4k9X` | `number` | Numeric field |  |
| **Reflexion**<br>`fldMhfdAsvfp74oEI` | `multilineText` | Multi-line text |  |
| **ObjetivoCumplido**<br>`fldRb8hae4XNP03q2` | `checkbox` | True/False checkbox |  |
| **ConversacionId**<br>`fld9fGB8RAarBx5kr` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 22. Suscripciones

*Table ID: `tblowJOhwqRvVsWWc`*
*Fields: 35*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Suscripcion**<br>`fldn1n7fwUweCvo2i` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldKyk6xVFuknhSHU` | `singleLineText` | Type: singleLineText |  |
| **EstudianteLink**<br>`fldRWKk87vRLaRL2M` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pagador**<br>`fldC8JSN5ogRs8ISq` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EmailPagador**<br>`fldpcfbuRcQaRsFlK` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **EstadoCuentaPagador**<br>`fldQqlZbunlfXfEsG` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **IDExternoPago**<br>`fldCbmS4gZ3LKmmqe` | `singleLineText` | Type: singleLineText |  |
| **Pago**<br>`fldILVnRROWcJJ9LU` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FechaPago**<br>`fldo8n5y0wZxhJ52M` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaProximoVencimiento**<br>`fldb1PSZ3mVGx4KS9` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Plan**<br>`fldaSqBvRS4GDaVI6` | `singleSelect` | Single choice dropdown | `Freemium`, `Premium`, `Premium Anual` |
| **OrigenPlan**<br>`fld5GOwJCP6Q65NY0` | `singleSelect` | Single choice dropdown | `Paddle`, `Beca`, `Promo` |
| **CodigoBeca **<br>`fld5n5OnZgqupfNXg` | `singleLineText` | Type: singleLineText |  |
| **Estado**<br>`fldi8RIHJ0G746lAr` | `singleSelect` | Single choice dropdown | `activa`, `cancelada`, `vencida`, `suspendida` |
| **FechaInicio**<br>`fldZSINYGUXmHqqJr` | `dateTime` | Date and time |  |
| **ConsultasUsadasSemana**<br>`fldwEhWwL1n2YCYmw` | `number` | Numeric field |  |
| **SemanaActual**<br>`fld59woiPrcvzibVY` | `date` | Date |  |
| **UltimoPago**<br>`fld3VQmUmMaUscPLg` | `dateTime` | Date and time |  |
| **MontoMensual**<br>`fldrYs1EXsSfvDAQY` | `currency` | Currency amount |  |
| **FechaCreacion**<br>`fldyLjf5pN8FOZtkB` | `createdTime` | Auto-generated creation time |  |
| **ProveedorPago**<br>`fld1kKM9eZ60X714E` | `singleSelect` | Single choice dropdown | `Paddle`, `MercadoPago` |
| **AfiliadoId**<br>`fldGeGII7htfSGMbC` | `singleLineText` | Type: singleLineText |  |
| **AfiliadoTipo**<br>`fld4yK0RNPkF9cGcB` | `singleSelect` | Single choice dropdown | `influencer`, `docente_ambassador`, `padre_embajador` |
| **ComisionPlan**<br>`fldSn2JJhZZkjUdUl` | `singleSelect` | Single choice dropdown | `recurrente_10`, `recurrente_20`, `primera_compra_30`, `custom` |
| **UTM_Source**<br>`fldbXzXvd8qLRpq6P` | `singleLineText` | Type: singleLineText |  |
| **UTM_Medium**<br>`fld7lXUePtLAFFBfk` | `singleLineText` | Type: singleLineText |  |
| **UTM_Campaign**<br>`fldLFoNMyI4WeCswy` | `singleLineText` | Type: singleLineText |  |
| **UltimoFalloPago**<br>`fldEHJVGJ48VA7Hrl` | `date` | Date |  |
| **IntentosReintento**<br>`fldlSDNBOmhy2yxMH` | `number` | Numeric field |  |
| **SuspendidaDesde**<br>`fldOOpOl9U4WLTFfH` | `date` | Date |  |
| **Pagos 2**<br>`fldCkH8WXaZ8OMUz9` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiantes**<br>`fldktDnYfToPEUlHK` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiantes copy**<br>`fldwYz1HMUFxlSUuB` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes 2**<br>`fldJQKk5HR7e9C8mV` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes 2 copy**<br>`fldngwoOT5egJSN7z` | `singleLineText` | Type: singleLineText |  |

---

## 📋 23. Testimonios

*Table ID: `tblMamG4VXbtJZNSd`*
*Fields: 22*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Testimonio**<br>`fldLPPjGgYFjrTUBB` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fld4AG3mcFaWpwuts` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **NombreMostrar**<br>`fldG9KdLMeKUE3gF9` | `singleLineText` | Type: singleLineText |  |
| **Edad**<br>`fld6dRJYRVhag0UWP` | `number` | Numeric field |  |
| **Texto**<br>`fldLoMVwRWEBpfpY8` | `multilineText` | Multi-line text |  |
| **ImagenURL**<br>`fldqfk4WI6CSYy0sO` | `url` | URL link |  |
| **Pais**<br>`fldtzOuum3vrMDcdX` | `singleSelect` | Single choice dropdown | `Argentina`, `Bolivia`, `Chile`, `Colombia`, `Ecuador` *(+7 more)* |
| **TiposNEE**<br>`fld00qa4CY0zNONTg` | `multipleSelects` | Multiple choice dropdown | `TDA`, `TDAH`, `TEA`, `Dislexia`, `Discalculia` *(+1 more)* |
| **ConversacionesAlEnviar**<br>`fldR1HqiuecBOT2kQ` | `number` | Numeric field |  |
| **FechaEnvio**<br>`fld8RXhYQO1GCgUHH` | `createdTime` | Auto-generated creation time |  |
| **Estado**<br>`fldSG4KwgwtQqO6ER` | `singleSelect` | Single choice dropdown | `Pendiente`, `Aprobado`, `Rechazado`, `Postergado` |
| **FechaRevision**<br>`fldJMArz5vIs2qjWK` | `dateTime` | Date and time |  |
| **NotasInternas**<br>`fld8tNgQeYXHpjJOk` | `multilineText` | Multi-line text |  |
| **MostrarEnLanding**<br>`fldAC5GZyNVxn7tKk` | `checkbox` | True/False checkbox |  |
| **MostrarAvisos**<br>`fldN79TbLpbkGuFWT` | `checkbox` | True/False checkbox |  |
| **Consentimiento**<br>`fldCEipr2tKeJqMej` | `checkbox` | True/False checkbox |  |
| **FechaConsentimiento**<br>`fldEp626LDM4xCmd0` | `dateTime` | Date and time |  |
| **Pregunta1**<br>`fldEtPCm0j7w1AvpI` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **Pregunta2**<br>`fldziGIfAiNiR6xfe` | `singleSelect` | Single choice dropdown | `Me ha servido mucho`, `Me ha servido algo`, `Me ha servido poco`, `No me ha servido` |
| **Pregunta3**<br>`fldPktTOTnXMWqiWE` | `singleSelect` | Single choice dropdown | `Mucho`, `Bastante`, `Algo`, `Nada` |
| **Pregunta4**<br>`fldmqLoWXkNJR89WW` | `singleSelect` | Single choice dropdown | `Aprender algo puntual`, `Preparar una evaluación`, `Aprender a estudiar` |
| **Pregunta5**<br>`fld8OpJJBBWb1H8K3` | `singleSelect` | Single choice dropdown | `Mucho, me asombra`, `Bastante`, `Lo percibo débilmente`, `No lo he notado` |

---

## 📋 24. VERSION_PROD

*Table ID: `tblStqh1QgUM2ZZGE`*
*Fields: 15*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **FechaPublicacion**<br>`fld4Vu39O4zNgLJqZ` | `dateTime` | Date and time |  |
| **Ambiente**<br>`fldj1wNtXh76HZvZR` | `singleSelect` | Single choice dropdown | `PROD`, `DEV` |
| **Descripción nueva versión**<br>`fldp4TVI2mIZYXWc4` | `multilineText` | Multi-line text |  |
| **Cambios BD**<br>`fldBSosvZGrV1Gt5J` | `singleLineText` | Type: singleLineText |  |
| **Descripción DB**<br>`fldLEbXdOc6yk9TI3` | `multipleAttachments` | Type: multipleAttachments |  |
| **Cambios Automatizaciones**<br>`fldNcmh2Qu8qVpwuh` | `singleLineText` | Type: singleLineText |  |
| **Archivos**<br>`fldWTvrKvV4UnvXZq` | `multipleAttachments` | Type: multipleAttachments |  |
| **landing.html**<br>`fldczEKFzscMX6JpS` | `multilineText` | Multi-line text |  |
| **index.html**<br>`fld7ECFpJRGQj4zJ8` | `multilineText` | Multi-line text |  |
| **chat.js**<br>`fldSdYMAXYd2d7Bob` | `multilineText` | Multi-line text |  |
| **config.js**<br>`fldrzHp2TJKe1Mrwn` | `multilineText` | Multi-line text |  |
| **Prompt-chat**<br>`fld1JoX5ky69KH0st` | `multilineText` | Multi-line text |  |
| **Worker**<br>`fldztpSTpYD3DvSlO` | `multilineText` | Multi-line text |  |
| **WorkerDeployment**<br>`fldYNzqOOvd62mNv8` | `singleLineText` | Type: singleLineText |  |
| **Version_Fillout_Onboarding**<br>`fldm1rmf4KOECMsfG` | `singleLineText` | Type: singleLineText |  |

---

## 🔄 About This Documentation

### 📋 Source Information
- **Base**: Default (`default`)
- **Base ID**: `app9c8iiAYRGxxhtH`
- **Generated**: 2026-03-26 09:06:47

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
**Last sync**: 2026-03-26 09:06:47

---
*Documentation for Default base - Generated 2026-03-26 09:06:47*