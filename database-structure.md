# 🗂️ Airtable Database Structure - Default

> **Last update**: 2026-07-26 10:06:46
> **Base**: default (Default)
> **Auto-generated** - Do not edit manually

## 📊 Summary

- **Tables**: 44
- **Total fields**: 989
- **Base ID**: `app9c8iiAYRGxxhtH`

- **singleSelect fields**: 90
- **multipleSelects fields**: 8
- **number fields**: 134
- **date fields**: 19
- **formula fields**: 20

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
*Fields: 32*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Conversacion**<br>`fldhpzpygAWASqIcm` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldsFM6LQCnmLIpev` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FechaAltaEstudiante**<br>`fldzwhZAcGxX19VAw` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **PlanActual**<br>`fldoqiJaCbFoR2N8Z` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TipoPuerta**<br>`fldfGrwAFFXcL5jos` | `singleSelect` | Single choice dropdown | `aprender`, `preparar-evaluacion`, `estudiar`, `mejorar-habitos`, `prepararme-paes` |
| **Titulo**<br>`fldNkHyWabgfGAThi` | `singleLineText` | Type: singleLineText |  |
| **MateriaPrincipal**<br>`fld6eG16Hs7av0euL` | `singleLineText` | Type: singleLineText |  |
| **TipoNEE**<br>`fldx65y33zQeiXOsi` | `singleLineText` | Type: singleLineText |  |
| **CantidadMensajes**<br>`fldQFSerbNJRUagkv` | `count` | Type: count |  |
| **CantidadMensajesFinal**<br>`fldNlONZcXOGV6s2M` | `number` | Numeric field |  |
| **Tokens**<br>`fldtCm0VWw3wvkt0V` | `rollup` | Rollup from linked records |  |
| **TokensCacheados**<br>`fld5yQeichwT2Nj1L` | `rollup` | Rollup from linked records |  |
| **TokensFinal**<br>`fldaYGwxvLqtSFKws` | `number` | Numeric field |  |
| **CostoAPI**<br>`fldvidJST7G3PhaTs` | `rollup` | Rollup from linked records |  |
| **CostoPromedioMensaje**<br>`fldflDIPvDSNKLDfr` | `formula` | Calculated field | Formula: `IF({fldQFSerbNJRUagkv}>0,
  ({fldvidJST7G3PhaTs}/...` |
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
*Fields: 26*

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
| **NivelEdadEstandar**<br>`fldOw4wRR9Mr3dkAh` | `formula` | Calculated field | Formula: `{fld2iZPfBxmNgBXA8}+6+0` |
| **OAnivelTxt**<br>`fldqX7bbGHJFCSJb9` | `singleSelect` | Single choice dropdown | `5° Básico`, `6° Básico`, `7° Básico`, `8° Básico` |
| **OAantiguedad**<br>`fldgT3bnJbcwkUnBD` | `number` | Numeric field |  |
| **OACodigoMineduc**<br>`fldhkAZ0yWLkzCZu9` | `formula` | Calculated field | Formula: `SWITCH(
  {fldPPTulbJihy1UmV},
  "Ciencias", "CN...` |
| **OASearchText**<br>`fldeoe85OhKHCV77f` | `formula` | Calculated field | Formula: `LOWER(
  {fldhkAZ0yWLkzCZu9} & " " &
  {fldPPTul...` |
| **OASearchKeywords**<br>`fldYqBharhQzGNjXv` | `aiText` | Type: aiText |  |
| **OAGDCardResumen**<br>`fldsGTp46pMHtclcM` | `aiText` | Type: aiText |  |
| **OAGDPreguntaDetonante**<br>`fldh56K4uI3FCb1n4` | `aiText` | Type: aiText |  |
| **OAGDClase**<br>`fld2aJKwI4eEyVb1Y` | `aiText` | Type: aiText |  |
| **OAGDCasa**<br>`fldnsb6xh1LlPC7wO` | `aiText` | Type: aiText |  |
| **OAGDDetectivePrompt**<br>`fldBnIFqvgLosfVN2` | `aiText` | Type: aiText |  |
| **OAGDCriteriosDocente**<br>`fld4eaBRKqCjFhyXk` | `aiText` | Type: aiText |  |

---

## 📋 6. EIA_Eventos

*Table ID: `tbljAbK5uN7tUNGzT`*
*Fields: 20*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EventoKey**<br>`fldVCsTcat2qUesQZ` | `autoNumber` | Type: autoNumber |  |
| **Evento**<br>`fldVReUxgwrIP6t9D` | `singleLineText` | Type: singleLineText |  |
| **Timestamp**<br>`fldwYb1LsIRSMlOt8` | `createdTime` | Auto-generated creation time |  |
| **SessionUUID**<br>`fldlSKOO45y99VXHp` | `singleLineText` | Type: singleLineText |  |
| **MetadataJSON**<br>`fldWIXg6dRGKn7BjF` | `multilineText` | Multi-line text |  |
| **UTMSource**<br>`flddjTdwBFrDLMPt9` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`flda51hBwkPuie2vY` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldhts5HjtgfRy8EZ` | `singleLineText` | Type: singleLineText |  |
| **PaisDetectadoIP**<br>`fldYL2GROmxCFHxS1` | `singleLineText` | Type: singleLineText |  |
| **RolDeclarado**<br>`fldcoPqz2WD6ofOFz` | `singleLineText` | Type: singleLineText |  |
| **SiteVersion**<br>`fldEYFKKfKRcSfZ5h` | `singleLineText` | Type: singleLineText |  |
| **WorkerVersion**<br>`fldFtYo5D2CF8qNqY` | `singleLineText` | Type: singleLineText |  |
| **Sesion**<br>`fldMlqrBUsD9Vb5XV` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Intento**<br>`fldjQ3K0cJcPQ3dSt` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **JourneyID**<br>`fldslLYrl9Ej3zPTy` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fld3eND3JUu09muf0` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldMOYaN1slZm03Jg` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fldZ2cpTekLA7K1Bd` | `singleLineText` | Type: singleLineText |  |
| **AppVersion**<br>`flds0Gt9L2gpOYkLh` | `singleLineText` | Type: singleLineText |  |
| **Environment**<br>`fld1rqE9QYQXTjocD` | `singleLineText` | Type: singleLineText |  |

---

## 📋 7. EIA_Intentos

*Table ID: `tbl80yft40YOSa6nD`*
*Fields: 34*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **IntentoKey**<br>`fldRNMDz3Ve9ptgLh` | `autoNumber` | Type: autoNumber |  |
| **CreatedAt**<br>`fld5S4oCFpDgpj8RA` | `createdTime` | Auto-generated creation time |  |
| **SessionUUID**<br>`fldBWfpLDCP0sjBfE` | `singleLineText` | Type: singleLineText |  |
| **ID_IntentoEIA**<br>`fldxYsWVxNKCsfEul` | `singleLineText` | Type: singleLineText |  |
| **NumeroIntento**<br>`fldn3Ox3BVDEJq0TK` | `number` | Numeric field |  |
| **EsValido**<br>`fldiyDblcdTOQ3bYU` | `checkbox` | True/False checkbox |  |
| **MotivoInvalido**<br>`fldsJx3xHBjHyfeUJ` | `singleLineText` | Type: singleLineText |  |
| **PromptUsuario**<br>`fld30LrmULvVYGpjW` | `multilineText` | Multi-line text |  |
| **PromptHash**<br>`fldAsWWVz18htEQbJ` | `singleLineText` | Type: singleLineText |  |
| **CriterioUsuario**<br>`fld2Dm47E39HqBk9K` | `multilineText` | Multi-line text |  |
| **RespuestaIA**<br>`fldr9oR5uuAWHfGlz` | `multilineText` | Multi-line text |  |
| **RespuestaFueLimitada**<br>`fldbWrdxezWgbDzM2` | `checkbox` | True/False checkbox |  |
| **CriticaEIA**<br>`fld9BP0qLoqUC2v9R` | `multilineText` | Multi-line text |  |
| **JSONCoach**<br>`fldpejhXM0Ybe4T3T` | `multilineText` | Multi-line text |  |
| **ScoreTotal**<br>`fld0TTderVa7Zsqmq` | `number` | Numeric field |  |
| **KPI_Claridad**<br>`fldk4fSLfrqa0TvZy` | `number` | Numeric field |  |
| **KPI_Precision**<br>`fldedb7UNQZLcRSGn` | `number` | Numeric field |  |
| **KPI_PensamientoPropio**<br>`fldscaRlp3Ap0DG6w` | `number` | Numeric field |  |
| **KPI_VerificacionCritica**<br>`fldx34RAE20gZZU0s` | `number` | Numeric field |  |
| **KPI_CuidadoAcademico**<br>`fldbtLqWoF4lUDN1K` | `number` | Numeric field |  |
| **Riesgo**<br>`fldgjvS3LTOuMPzlI` | `singleSelect` | Single choice dropdown | `verde`, `amarillo`, `rojo`, `invalido`, `etico` |
| **Nivel**<br>`fldBLkj0fZvnj7mxC` | `singleSelect` | Single choice dropdown | `modo_copia`, `modo_ayuda`, `modo_aprendiz`, `modo_copiloto`, `modo_detective` |
| **ModeloRespuesta**<br>`fldY48ImIH9VwpDxp` | `singleLineText` | Type: singleLineText |  |
| **ModeloCoach**<br>`fldZdtdYAnVL4dL60` | `singleLineText` | Type: singleLineText |  |
| **TokensInputRespuesta**<br>`fldbs68ax5xtu2hfu` | `number` | Numeric field |  |
| **TokensOutputRespuesta**<br>`fldSI0SK0oyiiQbhu` | `number` | Numeric field |  |
| **TokensInputCoach**<br>`fldLp0IVx50WwLE9P` | `number` | Numeric field |  |
| **TokensOutputCoach**<br>`fldQOTScBHKqhHbcR` | `number` | Numeric field |  |
| **CostoEstimado**<br>`fldhLdDVK9MuXPujF` | `number` | Numeric field |  |
| **Sesion**<br>`fldxij5neojr9BNtn` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EIA_Eventos**<br>`fldf2Erq0Z20GqWOo` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ModeloClassifier**<br>`fldgdFXqv78IS1K26` | `singleLineText` | Type: singleLineText |  |
| **TokensInputClassifier**<br>`fld73x82FvBfYZCM3` | `number` | Numeric field |  |
| **TokensOutputClassifier**<br>`fld7zLts8jgpbwoXF` | `number` | Numeric field |  |

---

## 📋 8. EIA_Sesiones

*Table ID: `tblFJmNzpszXfo1Rv`*
*Fields: 52*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_SesionEIA**<br>`fldsuU7YWbcieVaOu` | `autoNumber` | Type: autoNumber |  |
| **FechaInicio**<br>`fld8DwdtdCLlnmOGd` | `createdTime` | Auto-generated creation time |  |
| **RecordID**<br>`fldoxflUeBkbuikeg` | `formula` | Calculated field | Formula: `RECORD_ID()` |
| **SessionUUID**<br>`fldmOdV7PYZXjR0lz` | `singleLineText` | Type: singleLineText |  |
| **AnonID**<br>`fldrb7k6OFUVOp1y1` | `singleLineText` | Type: singleLineText |  |
| **Estudiante**<br>`fldgUQ5sD9kGZZ6yA` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Lead**<br>`fldxfF00F72fbyhMC` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **NombreCompleto**<br>`fldgvrQ8rIdSFvmJ8` | `singleLineText` | Type: singleLineText |  |
| **RolDeclarado**<br>`fldbNhNiaDytlL0mL` | `singleSelect` | Single choice dropdown | `estudiante`, `madre_padre_tutor`, `docente`, `estudios_superiores`, `otro` |
| **EmailGuardado**<br>`fldZEGmvMUlvic8k7` | `email` | Email address |  |
| **EdadDeclarada**<br>`fldq3anOdKGjNTzRs` | `number` | Numeric field |  |
| **FechaNacimiento**<br>`fldNNsRwUpIEyJ05s` | `date` | Date |  |
| **PaisDetectadoIP**<br>`fldeNV9Yzmx6RlMVv` | `singleLineText` | Type: singleLineText |  |
| **PaisElegido**<br>`fldEyughuqIHEL45P` | `singleSelect` | Single choice dropdown | `Chile`, `Colombia`, `Ecuador`, `Bolivia`, `Perú` *(+3 more)* |
| **IPHash**<br>`fldv8gOmo33mgk66N` | `singleLineText` | Type: singleLineText |  |
| **UserAgentHash**<br>`fldBMGhXTewWwBB5r` | `singleLineText` | Type: singleLineText |  |
| **RequiereConsentimientoParental**<br>`fldn4ZzITTgMmvpX3` | `checkbox` | True/False checkbox |  |
| **EstadoConsentimientoParental**<br>`fldxzOvpcN1Nwv9vV` | `singleSelect` | Single choice dropdown | `no_requerido`, `pendiente`, `otorgado`, `revocado` |
| **TutorNombre**<br>`fldujGhQ8kICcITeo` | `singleLineText` | Type: singleLineText |  |
| **TutorEmail**<br>`fldF5qyF8cnjbUD1G` | `email` | Email address |  |
| **TutorRelacion**<br>`fld6QCGFgGQO9HABi` | `singleSelect` | Single choice dropdown | `Padre`, `Madre`, `Tutor Legal` |
| **ConsentimientoPrivacidad**<br>`fldW4P4ol975fkufN` | `checkbox` | True/False checkbox |  |
| **FechaConsentimiento**<br>`fldBw7YEHKPmuF0Gr` | `dateTime` | Date and time |  |
| **VersionConsentimientoPrivacidad**<br>`fldf3rq6nEiJuZGkp` | `singleLineText` | Type: singleLineText |  |
| **VersionConsentimientoTerminos**<br>`fldtanljE35PFuw4I` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`fldmTciu1PCrdzFf3` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fld9Q8QNE9rJ8ytrh` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldJpB5jSfpKUnf1n` | `singleLineText` | Type: singleLineText |  |
| **Referrer**<br>`fldtOpN1r6CV8l0R9` | `url` | URL link |  |
| **ShareIDOrigen**<br>`fldzHlXM26DjESXVz` | `singleLineText` | Type: singleLineText |  |
| **IntentosValidos**<br>`fldkd9nftBFfVWTjt` | `number` | Numeric field |  |
| **ScoreInicial**<br>`fldltB9ANb3QgKawW` | `number` | Numeric field |  |
| **ScoreFinal**<br>`fldPHB86Xvf6nCZSz` | `number` | Numeric field |  |
| **NivelInicial**<br>`fldXQVYkLJzPWlnMG` | `singleSelect` | Single choice dropdown | `modo_copia`, `modo_ayuda`, `modo_aprendiz`, `modo_copiloto`, `modo_detective` |
| **NivelFinal**<br>`fldUHSBjcNgsqC98V` | `singleSelect` | Single choice dropdown | `modo_copia`, `modo_ayuda`, `modo_aprendiz`, `modo_copiloto`, `modo_detective` |
| **RiesgoInicial**<br>`fldzaO9EuoCnz2aBO` | `singleSelect` | Single choice dropdown | `verde`, `amarillo`, `rojo`, `invalido` |
| **RiesgoFinal**<br>`fldGLMechioDz5TL9` | `singleSelect` | Single choice dropdown | `verde`, `amarillo`, `rojo`, `invalido` |
| **ModoDetectiveUsado**<br>`fldmTBZVrv8w4I0Z7` | `checkbox` | True/False checkbox |  |
| **Completada**<br>`fldwH0TuB4eVEy44z` | `checkbox` | True/False checkbox |  |
| **TipoCierre**<br>`fldqtWfhEYnjNDktP` | `singleSelect` | Single choice dropdown | `completada`, `abandono_datos`, `abandono_prompt`, `abandono_critica`, `limite` *(+2 more)* |
| **ClickWhatsApp**<br>`fldkhHuB4vIaNIYq6` | `checkbox` | True/False checkbox |  |
| **ClickKoruFreemium**<br>`fldD24xUSQIE7FM27` | `checkbox` | True/False checkbox |  |
| **FechaTermino**<br>`fldTv4P9UlRKFFHwV` | `dateTime` | Date and time |  |
| **DuracionSegundos**<br>`fldNLSqDHHpKJU7My` | `number` | Numeric field |  |
| **CostoTotalEstimado**<br>`fldhaCu51ym2DmZWO` | `number` | Numeric field |  |
| **TokensInputTotal**<br>`fldGk3CBBrXlzqD4x` | `number` | Numeric field |  |
| **TokensOutputTotal**<br>`fld839D4pe5Ug9DAt` | `number` | Numeric field |  |
| **ModeloCoachUltimo**<br>`fldCZDrRwnzvrp33S` | `singleLineText` | Type: singleLineText |  |
| **ModeloRespuestaUltimo**<br>`fld3pMzWmerDW17x7` | `singleLineText` | Type: singleLineText |  |
| **EIA_Intentos**<br>`fldiPIq0uPr2jHz04` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EIA_Eventos**<br>`fld2dt8esd4VVtamW` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EIA_Shares**<br>`fldHu6q3OkesRPQtH` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 9. EIA_Shares

*Table ID: `tblUzAlUePvcwsHBz`*
*Fields: 11*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ShareID**<br>`fldHOB6hiKMZyKhI0` | `singleLineText` | Type: singleLineText |  |
| **ID_ShareEIA**<br>`fld2N8Ca7bRdaJn5M` | `singleLineText` | Type: singleLineText |  |
| **TipoShare**<br>`fldx9SLe8FIjVhiRw` | `singleLineText` | Type: singleLineText |  |
| **URLGenerada**<br>`fldNxdyaKNC6XUf74` | `url` | URL link |  |
| **MensajeSugerido**<br>`fldDcP99gCezIOrrO` | `multilineText` | Multi-line text |  |
| **Clicks**<br>`fldKkrVkPxCugJ4b2` | `number` | Numeric field |  |
| **RegistrosAtribuidos**<br>`fld3KVzAltjVsOfhp` | `number` | Numeric field |  |
| **SesionesAtribuidas**<br>`fldNhqVN01PiF9si3` | `number` | Numeric field |  |
| **CreatedAt**<br>`fldPRsYX9W0Pbq9hD` | `createdTime` | Auto-generated creation time |  |
| **UltimoClick**<br>`fldf513i1wMUx5FIG` | `dateTime` | Date and time |  |
| **SesionOrigen**<br>`fldiDWFIyJp4PgUP2` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 10. EjemplosPedagogicos

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

## 📋 11. Estudiantes

*Table ID: `tblR5gbkydy59GOOC`*
*Fields: 121*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Estudiante**<br>`fldp7qIUatWYG2zw2` | `autoNumber` | Type: autoNumber |  |
| **Email**<br>`fldaPohMI9tlgDW4t` | `email` | Email address |  |
| **IDExternoPago**<br>`fld6P8XQEE3SNZy7X` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **SesionActivaToken**<br>`fldeNdxf94vhx95qp` | `singleLineText` | Type: singleLineText |  |
| **SesionActivaDeviceId**<br>`fld8hno4n2Q0byffc` | `singleLineText` | Type: singleLineText |  |
| **UltimaActividad**<br>`fld00gaBZOkktKJYO` | `dateTime` | Date and time |  |
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
| **LlegoPor**<br>`fld51E4NaVZvq9upz` | `singleSelect` | Single choice dropdown | `Aviso en Facebook`, `Aviso en Instagram`, `ChatGPT u otra IA`, `Convenio con tu colegio`, `Google` *(+8 more)* |
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
| **DiasDesdeUltima**<br>`fldYd2NI4ued8FXc7` | `formula` | Calculated field | Formula: `DATETIME_DIFF(
     SET_TIMEZONE(NOW(), 'America/...` |
| **CantidadConversacionesDeDias**<br>`fldkF1lllYaBcR4Bl` | `formula` | Calculated field | Formula: `{fldJZJ0PotO13gABR}+{fldA3hx5Y8HUCQQxe}+{fldT3F5dU...` |
| **CostoConversaciones**<br>`fldHvqFKsA5x7fNaS` | `rollup` | Rollup from linked records |  |
| **CostoPromedioConversacion**<br>`fld5DQxqWhbeRvlwN` | `formula` | Calculated field | Formula: `IF({fldkF1lllYaBcR4Bl}>0,
  {fldHvqFKsA5x7fNaS}/{...` |
| **CantidadConversacionesExitosas**<br>`fldY1vwqXfZLzzn2W` | `count` | Type: count |  |
| **CantidadConversacionesTotales**<br>`fld3EuETc0w2ZsgZr` | `count` | Type: count |  |
| **DiaPreferido**<br>`fldVjrwPqDhBFZOVa` | `formula` | Calculated field | Formula: `IF(AND({fldJZJ0PotO13gABR}>={fldA3hx5Y8HUCQQxe},{f...` |
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
| **EIA_Sesiones**<br>`fldjgTqy6phK9R1Bs` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **SeñalesDeInteres**<br>`fldf0NM2s3OmDEKZy` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ModifiedTime**<br>`fldtvTwCetCgGtmYp` | `lastModifiedTime` | Auto-generated modification time |  |

---

## 📋 12. Events

*Table ID: `tblmuAev9phNXJoF3`*
*Fields: 39*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EventID**<br>`fldCVq8xSTRRmoEQv` | `singleLineText` | Type: singleLineText |  |
| **EventName**<br>`fld9yv9rI0O4Grq2e` | `singleLineText` | Type: singleLineText |  |
| **JourneyID**<br>`fldujKwvrNn3VRTDT` | `singleLineText` | Type: singleLineText |  |
| **EventTime**<br>`fldkMSmHlvmui1AmE` | `dateTime` | Date and time |  |
| **ReceivedAt**<br>`fldRXTv1xDwHITv1H` | `dateTime` | Date and time |  |
| **IdempotencyKey**<br>`fldbFD0GKJVurYhfI` | `singleLineText` | Type: singleLineText |  |
| **Environment**<br>`fldDSkV083gEfNcO7` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fldevF2WYo7HmgEkp` | `singleLineText` | Type: singleLineText |  |
| **AppVersion**<br>`fldwU25KP4rPsMJPk` | `singleLineText` | Type: singleLineText |  |
| **WorkerVersion**<br>`fldt4kJjVemHvNDEN` | `singleLineText` | Type: singleLineText |  |
| **PropertiesJSON**<br>`fldlwf0TYmNsl65pG` | `multilineText` | Multi-line text |  |
| **CountryDetected**<br>`fldwxAUEZTWKilh0Q` | `singleLineText` | Type: singleLineText |  |
| **CountrySelected**<br>`fld1f0RoL8vrAszqT` | `singleLineText` | Type: singleLineText |  |
| **CountryForAnalysis**<br>`fldFqoxayymyvIVnd` | `singleLineText` | Type: singleLineText |  |
| **AnonID**<br>`fldwmci6Q06oYpqiN` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldca048w6rsTTT2D` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldQ8pP4Eh2OI12BJ` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldsiTMjoTJFqhUTb` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldmxbzNyDVZWdQ6S` | `singleLineText` | Type: singleLineText |  |
| **SessionID**<br>`fldNoKzA5RubL3aZV` | `singleLineText` | Type: singleLineText |  |
| **TouchpointID**<br>`fldSUTqNxxRZcrIHN` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldLJkLfdxJg8Q6aC` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`flduwWNd1LYuUrCba` | `singleLineText` | Type: singleLineText |  |
| **InstitutionID**<br>`fldjYsQEWpDDmcAzK` | `singleLineText` | Type: singleLineText |  |
| **CohortID**<br>`fld2RwM0K9YTrSs8b` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`fldRsCXw6TztJvaqP` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldtSNAGBuang0Btl` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldKcxLkd8QWAaElG` | `singleLineText` | Type: singleLineText |  |
| **UTMContent**<br>`fldGCI92HuAjm3AmJ` | `singleLineText` | Type: singleLineText |  |
| **UTMTerm**<br>`flddVbMWhfp6TPVbu` | `singleLineText` | Type: singleLineText |  |
| **Fbclid**<br>`fld3ll6X3vrxybuDw` | `singleLineText` | Type: singleLineText |  |
| **Referrer**<br>`fld2ezShryGaUhEN0` | `multilineText` | Multi-line text |  |
| **PageURL**<br>`fld79g0piBOr8rspb` | `multilineText` | Multi-line text |  |
| **RootJourneyID**<br>`fldI6UX3oFpqMTE2m` | `singleLineText` | Type: singleLineText |  |
| **ParentJourneyID**<br>`fldZrYjxsvppL7vmR` | `singleLineText` | Type: singleLineText |  |
| **ReferralID**<br>`fldo2zVqW5cKM62PL` | `singleLineText` | Type: singleLineText |  |
| **Gclid**<br>`fldhvcH3zZC5ICc9L` | `singleLineText` | Type: singleLineText |  |
| **EventSource**<br>`fld5BN0OYAqw9p6rS` | `singleLineText` | Type: singleLineText |  |
| **SchemaVersion**<br>`fldU6Xzijlk3xFdzI` | `singleLineText` | Type: singleLineText |  |

---

## 📋 13. GrowthAnalysis

*Table ID: `tbl6wrx1FNs9OzcT3`*
*Fields: 15*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **AnalysisID**<br>`fldhY0DM1LBgdrqGr` | `singleLineText` | Type: singleLineText |  |
| **AnalysisType**<br>`fld5Q2RmBPwdfym58` | `singleLineText` | Type: singleLineText |  |
| **PeriodStart**<br>`fld8c5mhhd9n0FgGM` | `dateTime` | Date and time |  |
| **PeriodEnd**<br>`fldlkCPSVPWul1Hjq` | `dateTime` | Date and time |  |
| **DataSnapshotID**<br>`fldsqO8XV6gfSiy2o` | `singleLineText` | Type: singleLineText |  |
| **ExecutiveSummary**<br>`fldcpXJx0QaJBGpX8` | `multilineText` | Multi-line text |  |
| **Findings**<br>`fldlURvfVsd16MsFA` | `multilineText` | Multi-line text |  |
| **Anomalies**<br>`fldPYxd155OpXMNX3` | `multilineText` | Multi-line text |  |
| **SegmentsToAct**<br>`fldDMDItMb6WeHuBb` | `multilineText` | Multi-line text |  |
| **Hypotheses**<br>`fldqqeVdFMdP4SHus` | `multilineText` | Multi-line text |  |
| **RecommendedActions**<br>`fldKpv93ZUSSAepKD` | `multilineText` | Multi-line text |  |
| **Priority**<br>`fldDc0bmtRVwyNEGi` | `singleLineText` | Type: singleLineText |  |
| **HumanDecision**<br>`fldDCN3s3DBX820Bo` | `multilineText` | Multi-line text |  |
| **ActionStatus**<br>`fldmsKrjaLKaT2PCO` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldIvXXmSaDFHrHCU` | `dateTime` | Date and time |  |

---

## 📋 14. EventosSignificativos

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

## 📋 15. IdentityMap

*Table ID: `tblRIoIJVSqDU32wX`*
*Fields: 35*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **IdentityKey**<br>`fld5lOnCRP7yVfBdR` | `singleLineText` | Type: singleLineText |  |
| **AnonID**<br>`fldz02zeHVEB9pLlT` | `singleLineText` | Type: singleLineText |  |
| **DeviceID**<br>`fldiKD2pTtysZhDxy` | `singleLineText` | Type: singleLineText |  |
| **Email**<br>`fldPXzTcsmtregGS4` | `singleLineText` | Type: singleLineText |  |
| **EmailHash**<br>`fldJQjygjiO2emt6I` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldDZOqzpLZlDeFE5` | `singleLineText` | Type: singleLineText |  |
| **LeadID**<br>`fldGh6ZNrSxhAMLjN` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldHdKhJWT3T2gcqx` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldhQ4r1evA9gZAma` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldfC5SG498WTk0Sl` | `singleLineText` | Type: singleLineText |  |
| **FirstSeenAt**<br>`fldUD5Pa063sLMoRA` | `dateTime` | Date and time |  |
| **LastSeenAt**<br>`fldBoh8UJdDT6AeRE` | `dateTime` | Date and time |  |
| **Confidence**<br>`fldT9dCV4VoKDKcBB` | `singleLineText` | Type: singleLineText |  |
| **Source**<br>`fldkrN8ZapK9QcY7s` | `singleLineText` | Type: singleLineText |  |
| **IdentificationLevel**<br>`fldzQg0NVgegGdQOn` | `singleLineText` | Type: singleLineText |  |
| **IsIdentified**<br>`fldadg8FAjg34L2di` | `checkbox` | True/False checkbox |  |
| **Environment**<br>`fld1oK2EmJHFOEoIn` | `singleLineText` | Type: singleLineText |  |
| **FirstJourneyID**<br>`fldC7N0ED7qcilG9j` | `singleLineText` | Type: singleLineText |  |
| **LastJourneyID**<br>`fld5lznshOKzwvKBG` | `singleLineText` | Type: singleLineText |  |
| **RootJourneyID**<br>`flduFwGr6BpPdEcLm` | `singleLineText` | Type: singleLineText |  |
| **FirstEventID**<br>`fldJQPFxQtSPYdmtE` | `singleLineText` | Type: singleLineText |  |
| **FirstEventName**<br>`fldDrhH2rYISXau76` | `singleLineText` | Type: singleLineText |  |
| **FirstEventTime**<br>`flddMw9eYNmx1zxGV` | `dateTime` | Date and time |  |
| **FirstEventRecordID**<br>`fldIlrK8gCjL438gp` | `singleLineText` | Type: singleLineText |  |
| **LastEventID**<br>`fldJFupj9ri9pPoCR` | `singleLineText` | Type: singleLineText |  |
| **LastEventName**<br>`fldSzIYfJ3yFxCo85` | `singleLineText` | Type: singleLineText |  |
| **LastEventTime**<br>`fldKOJfCaun6npacB` | `dateTime` | Date and time |  |
| **LastEventRecordID**<br>`fldyQ6JBd1hchCvqB` | `singleLineText` | Type: singleLineText |  |
| **FirstProductContext**<br>`fldi2yWySfzH3jsmz` | `singleLineText` | Type: singleLineText |  |
| **LastProductContext**<br>`fldVP6OGJorTafo8R` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldlTRJn5fskK4c49` | `dateTime` | Date and time |  |
| **UpdatedAt**<br>`fldS5ZZN6ZiwPBwGw` | `dateTime` | Date and time |  |
| **EventCount**<br>`fldbY3MPVEg6W5aHl` | `number` | Numeric field |  |
| **LastPageURL**<br>`fldc37TjTloGH5o2X` | `multilineText` | Multi-line text |  |
| **LastPropertiesJSON**<br>`fld64Hal6Rw5oqRUX` | `multilineText` | Multi-line text |  |

---

## 📋 16. Interventions

*Table ID: `tbldwEc4pjgfCAIVf`*
*Fields: 20*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **InterventionID**<br>`fldb9a5MNyOu91bJV` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldCOPPvf1l0CLlFk` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldafYjC56IIu6AA5` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldhYwkTpDEmRH5ZM` | `singleLineText` | Type: singleLineText |  |
| **InterventionType**<br>`fldYoMpklMuvTVRkS` | `singleLineText` | Type: singleLineText |  |
| **TriggerReason**<br>`fldUAI9SMFAG1bVzX` | `multilineText` | Multi-line text |  |
| **TriggerEventID**<br>`fldd9OsbmLWPRgnbu` | `singleLineText` | Type: singleLineText |  |
| **LifecycleStageAtTrigger**<br>`fldTowfywssvAdSOE` | `singleLineText` | Type: singleLineText |  |
| **CreditsGranted**<br>`fldKlvBdtdq5ibCzE` | `number` | Numeric field |  |
| **CreditsType**<br>`fldqQBDoG2MrWZ0iC` | `singleLineText` | Type: singleLineText |  |
| **MessageSent**<br>`fldc27ttxgjW1QdT6` | `multilineText` | Multi-line text |  |
| **Channel**<br>`fldepKUp3xA5xxxEg` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldyeXuWQepXsAag2` | `dateTime` | Date and time |  |
| **DeliveredAt**<br>`fldLrtaMbGecUBxDN` | `dateTime` | Date and time |  |
| **OpenedAt**<br>`fldkywMc94VO1IquH` | `dateTime` | Date and time |  |
| **ClickedAt**<br>`fldViX6iUIGw27zlP` | `dateTime` | Date and time |  |
| **RedeemedAt**<br>`fldFCYaK1w9YAUulU` | `dateTime` | Date and time |  |
| **OutcomeWindowDays**<br>`fldKk3TPOwNnrSdBS` | `number` | Numeric field |  |
| **OutcomeEvent**<br>`fldE5sDObyIt7YlHh` | `singleLineText` | Type: singleLineText |  |
| **OutcomeSuccess**<br>`fldWZ8GHHrF2Tid2E` | `checkbox` | True/False checkbox |  |

---

## 📋 17. Institutions

*Table ID: `tbl65wIkkQhADQARg`*
*Fields: 12*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **InstitutionID**<br>`fldZKrX7kcd0kNyjW` | `singleLineText` | Type: singleLineText |  |
| **Country**<br>`fldGoseduDCZyaZip` | `singleLineText` | Type: singleLineText |  |
| **InstitutionOfficialID**<br>`fldvsn9MW6zdlupiT` | `singleLineText` | Type: singleLineText |  |
| **InstitutionOfficialIDType**<br>`fldqOcfINXHULostg` | `singleLineText` | Type: singleLineText |  |
| **InstitutionName**<br>`fldsdxjp4rrenwCds` | `singleLineText` | Type: singleLineText |  |
| **City**<br>`fldNAcdVfUMydDGhM` | `singleLineText` | Type: singleLineText |  |
| **Commune**<br>`fldu8YetulLPrQ8O3` | `singleLineText` | Type: singleLineText |  |
| **Region**<br>`fldM1SuIiEY81eeTn` | `singleLineText` | Type: singleLineText |  |
| **AgreementStatus**<br>`fld9Pi2MZjHwbaO9K` | `singleLineText` | Type: singleLineText |  |
| **AgreementStartDate**<br>`fldsLGL3eT4wEihkX` | `date` | Date |  |
| **AgreementEndDate**<br>`fldLOmvf0ycMZy9L5` | `date` | Date |  |
| **EIAAccessLevel**<br>`fldsMEpDG02EijRys` | `singleLineText` | Type: singleLineText |  |

---

## 📋 18. InstitutionCohorts

*Table ID: `tblLZB34VcPdzlvtQ`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **CohortID**<br>`fldJoFw3z5wGq3ejU` | `singleLineText` | Type: singleLineText |  |
| **InstitutionID**<br>`flddDYtwJdBfE1Dey` | `singleLineText` | Type: singleLineText |  |
| **Country**<br>`fldPTRZaYaoYYvwpu` | `singleLineText` | Type: singleLineText |  |
| **AcademicYear**<br>`fldvQYqYzXrlN4HAs` | `singleLineText` | Type: singleLineText |  |
| **LevelCanonical**<br>`fldWo1wZT0Ol7LyLs` | `number` | Numeric field |  |
| **CourseSection**<br>`fldMtnta1GF08c44k` | `singleLineText` | Type: singleLineText |  |
| **CourseCanonical**<br>`fld8o2drZ9Cma1cUM` | `singleLineText` | Type: singleLineText |  |
| **CourseLocalLabel**<br>`fldnqaADg45i904fu` | `singleLineText` | Type: singleLineText |  |
| **EIAAccessLevel**<br>`fldrTSgE6B8EK3RnT` | `singleLineText` | Type: singleLineText |  |

---

## 📋 19. InstitutionStudentValidation

*Table ID: `tbl8Ye6EgsTglQFJb`*
*Fields: 8*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ValidationID**<br>`fldPuoBuhJqbFa0vG` | `singleLineText` | Type: singleLineText |  |
| **InstitutionID**<br>`fldV2yFaPgmFP4kYY` | `singleLineText` | Type: singleLineText |  |
| **CohortID**<br>`fldhTDhtKPJmUWgap` | `singleLineText` | Type: singleLineText |  |
| **StudentNationalIDHash**<br>`fldT1mVLG7rxUPVM8` | `singleLineText` | Type: singleLineText |  |
| **StudentNationalIDLast4**<br>`fldlFnuYXRaiOBDWT` | `singleLineText` | Type: singleLineText |  |
| **Status**<br>`fldRGfpCubGkCMdEm` | `singleLineText` | Type: singleLineText |  |
| **ValidationMethod**<br>`fldXmELT505I5OA41` | `singleLineText` | Type: singleLineText |  |
| **LastValidatedAt**<br>`fldJYAmql6gnZoqff` | `dateTime` | Date and time |  |

---

## 📋 20. Journeys

*Table ID: `tbl446CakE2I9mAv5`*
*Fields: 101*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **JourneyID**<br>`fldUxhE1f0YCw0xQC` | `singleLineText` | Type: singleLineText |  |
| **RootJourneyID**<br>`fldAqPhM866XvfhfF` | `singleLineText` | Type: singleLineText |  |
| **CurrentStage**<br>`fldLIng1uFdzlfBR6` | `singleLineText` | Type: singleLineText |  |
| **LastEventName**<br>`fldjHaeZt2enD0TQ5` | `singleLineText` | Type: singleLineText |  |
| **FirstEventName**<br>`fldjJuHtzix0I2h8f` | `singleLineText` | Type: singleLineText |  |
| **FirstEventID**<br>`fldCBEUkSzVXBTqii` | `singleLineText` | Type: singleLineText |  |
| **FirstEventTime**<br>`flduncpcG6L6Xs41z` | `dateTime` | Date and time |  |
| **FirstEventRecordID**<br>`fldrwnjEGCnA0b1kP` | `singleLineText` | Type: singleLineText |  |
| **RootAnonID**<br>`fldU5uaNt6g26CGnB` | `singleLineText` | Type: singleLineText |  |
| **RootPersonID**<br>`fldgdHxmuMEyb8KCl` | `singleLineText` | Type: singleLineText |  |
| **FirstTouchpointID**<br>`fldpqCQjU7OErP36x` | `singleLineText` | Type: singleLineText |  |
| **FirstSeenAt**<br>`fldI8hsvidseMC1uN` | `dateTime` | Date and time |  |
| **LastSeenAt**<br>`fldax0m7wVPb0wnWx` | `dateTime` | Date and time |  |
| **AcquisitionPath**<br>`fldVJlVb8wZvA5vyQ` | `multilineText` | Multi-line text |  |
| **FirstTouchChannel**<br>`fldgZMdcfapwksgUT` | `singleLineText` | Type: singleLineText |  |
| **FirstTouchCampaign**<br>`fldNFxVBT8otx4gez` | `singleLineText` | Type: singleLineText |  |
| **LastTouchChannel**<br>`fldLKGSxLcdf8q6Z6` | `singleLineText` | Type: singleLineText |  |
| **LastTouchCampaign**<br>`fldNiY66NaZBbdm1K` | `singleLineText` | Type: singleLineText |  |
| **RootChainChannel**<br>`fldaHAD63IZJGU7CP` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fld5eeHsMZv5fxdj2` | `singleLineText` | Type: singleLineText |  |
| **ShareDepthMax**<br>`fldELdDPn5EOs1L9u` | `number` | Numeric field |  |
| **HasMother**<br>`flduLRdzhaNVIu5Ix` | `checkbox` | True/False checkbox |  |
| **HasStudent**<br>`flduKA7hOZmlzcJUD` | `checkbox` | True/False checkbox |  |
| **HasInstitution**<br>`fldtZbqZKhvaCO98T` | `checkbox` | True/False checkbox |  |
| **HasEIA**<br>`fldbjEWBqy7d76YAS` | `checkbox` | True/False checkbox |  |
| **HasKoruFreemium**<br>`fldIkoTFq3bYgHVLN` | `checkbox` | True/False checkbox |  |
| **HasKoruActivation**<br>`fldBEYpVA3Gcl71hR` | `checkbox` | True/False checkbox |  |
| **HasPremium**<br>`fldKCwIhBluP0OpbZ` | `checkbox` | True/False checkbox |  |
| **PremiumStartedAt**<br>`fld9dz2wZmqRBpMik` | `dateTime` | Date and time |  |
| **CurrentLTV**<br>`fldpuDmRmvWfKr6VJ` | `number` | Numeric field |  |
| **ParentJourneyID**<br>`fldT48LJ2G7iiS0tG` | `singleLineText` | Type: singleLineText |  |
| **Environment**<br>`fld1hLuMg78vx01Hv` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fld0i5lfM2fnQeEy3` | `singleLineText` | Type: singleLineText |  |
| **Status**<br>`fldsZGWhjNsAiifMD` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fld13U9XmITkHX1oX` | `dateTime` | Date and time |  |
| **UpdatedAt**<br>`fld52ttKA1xt0Z0N6` | `dateTime` | Date and time |  |
| **LastEventID**<br>`fldXPdOQXMWLoZkTy` | `singleLineText` | Type: singleLineText |  |
| **LastEventTime**<br>`fldUV94XObnxmjmAP` | `dateTime` | Date and time |  |
| **LastEventRecordID**<br>`fldqEHblvF74HsiSf` | `singleLineText` | Type: singleLineText |  |
| **EventCount**<br>`fldcBjVdAixsoRDBI` | `number` | Numeric field |  |
| **AnonID**<br>`fldRS572EcrO6Ljam` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldCRabW7woesirGW` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldulu8VvB6dXo9e4` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldthBP6HBqKH8T6u` | `singleLineText` | Type: singleLineText |  |
| **CountryDetected**<br>`fldjhDCB9LeUWWeUI` | `singleLineText` | Type: singleLineText |  |
| **CountrySelected**<br>`fldtIBmuL9HZpylzl` | `singleLineText` | Type: singleLineText |  |
| **CountryForAnalysis**<br>`fldf7A1q13uv97OeL` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`fldSoh8QQfA1udEkW` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldJzy0gtTIMWuVWj` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldYFjmlTmDsnSETq` | `singleLineText` | Type: singleLineText |  |
| **UTMContent**<br>`fldQbNuIewXcvCYsO` | `singleLineText` | Type: singleLineText |  |
| **UTMTerm**<br>`fldfdFIKuQaYh0xqo` | `singleLineText` | Type: singleLineText |  |
| **Fbclid**<br>`fldXjCMo2RfqGhqwo` | `singleLineText` | Type: singleLineText |  |
| **Gclid**<br>`fldIKHNJ496B8z8j5` | `singleLineText` | Type: singleLineText |  |
| **Referrer**<br>`fldRw270F8Du6eoZ9` | `singleLineText` | Type: singleLineText |  |
| **LandingPageURL**<br>`fldLZOSzBN6KJjHI7` | `singleLineText` | Type: singleLineText |  |
| **LastPageURL**<br>`fldJVZkDRUUb90j2s` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldToglfKM7D9biC0` | `singleLineText` | Type: singleLineText |  |
| **ReferralID**<br>`fldnaldhTSDudfe9n` | `singleLineText` | Type: singleLineText |  |
| **FirstPropertiesJSON**<br>`fldBWcVuptBBAmXLe` | `multilineText` | Multi-line text |  |
| **LastPropertiesJSON**<br>`fldwaO2e0mn20WU8a` | `multilineText` | Multi-line text |  |
| **HasQualifiedVisit**<br>`fldrvRvqpTlBM3mVv` | `checkbox` | True/False checkbox |  |
| **QualifiedVisitAt**<br>`fldCMv9rlMASVIVxl` | `dateTime` | Date and time |  |
| **HasCTAClicked**<br>`fldn2bD7WLVHFDxSR` | `checkbox` | True/False checkbox |  |
| **FirstCTAClickedAt**<br>`fld5KKgf73cIP23P3` | `dateTime` | Date and time |  |
| **HasEIAStarted**<br>`fldvJ3FTLpFdzAZjm` | `checkbox` | True/False checkbox |  |
| **EIAStartedAt**<br>`fldjJ9NF0HxcRN3Og` | `dateTime` | Date and time |  |
| **HasEIACompleted**<br>`fldEqr7YHzgzvZJbg` | `checkbox` | True/False checkbox |  |
| **EIACompletedAt**<br>`fld0dRMaAqRydCFLN` | `dateTime` | Date and time |  |
| **HasSignupStarted**<br>`fld4Sx1wfsiYqkjid` | `checkbox` | True/False checkbox |  |
| **SignupStartedAt**<br>`fldHcg7SmrKwNE4nU` | `dateTime` | Date and time |  |
| **FreemiumRegisteredAt**<br>`fldmUFNZovXew2kqi` | `dateTime` | Date and time |  |
| **HasFreemiumRegistered**<br>`fldjjvDsjf1yWQvnp` | `checkbox` | True/False checkbox |  |
| **HasFirstSessionStarted**<br>`fldwFkHCIfU9Jc0Nd` | `checkbox` | True/False checkbox |  |
| **FirstSessionStartedAt**<br>`fld0O2onEoB13KXMW` | `dateTime` | Date and time |  |
| **HasFirstSessionCompleted**<br>`fldLxQat5mTa3iEaO` | `checkbox` | True/False checkbox |  |
| **FirstSessionCompletedAt**<br>`fldwptYmvVZCfGrn4` | `dateTime` | Date and time |  |
| **HasSecondSessionCompleted**<br>`fldIeuOwLTAL1lyMI` | `checkbox` | True/False checkbox |  |
| **SecondSessionCompletedAt**<br>`fldOody15UXc8maZ0` | `dateTime` | Date and time |  |
| **HasActivationAchieved**<br>`fld5gXueW2IqofHwo` | `checkbox` | True/False checkbox |  |
| **ActivationAchievedAt**<br>`fld9fbfFPRa8vocZy` | `dateTime` | Date and time |  |
| **HasPremiumCheckoutStarted**<br>`fld7mB853sar2owo7` | `checkbox` | True/False checkbox |  |
| **PremiumCheckoutStartedAt**<br>`fld3Dy9xhXCTW61IS` | `dateTime` | Date and time |  |
| **HasPremiumPaymentCompleted**<br>`fld3iGNY1SSI28R0d` | `checkbox` | True/False checkbox |  |
| **PremiumPaymentCompletedAt**<br>`fld41ixxgz17RX5SM` | `dateTime` | Date and time |  |
| **HasPremiumStarted**<br>`fld4las0kp6FxNYTe` | `checkbox` | True/False checkbox |  |
| **FirstTouchCapturedAt**<br>`fldjdyToulVJyEOsk` | `dateTime` | Date and time |  |
| **LastTouchCapturedAt**<br>`fld3dU6k1m8enxY56` | `dateTime` | Date and time |  |
| **LastUTMSource**<br>`fldXKUdJCTrjPoOrS` | `singleLineText` | Type: singleLineText |  |
| **LastUTMMedium**<br>`fldtuSEtitpwEtJWo` | `singleLineText` | Type: singleLineText |  |
| **LastUTMCampaign**<br>`fldQyHeE0zrsCPbNJ` | `singleLineText` | Type: singleLineText |  |
| **LastUTMContent**<br>`fldgiybcfUZTLD91h` | `singleLineText` | Type: singleLineText |  |
| **LastUTMTerm**<br>`fldGzqWIAMfS4jV43` | `singleLineText` | Type: singleLineText |  |
| **LastFbclid**<br>`flddpPi6U0a1OAa55` | `singleLineText` | Type: singleLineText |  |
| **LastGclid**<br>`fldk4vdZlb3hAsvXg` | `singleLineText` | Type: singleLineText |  |
| **LastReferrer**<br>`fldNKRA544Ji89cxg` | `multilineText` | Multi-line text |  |
| **LastTouchEventID**<br>`fldhxHjZBBuW0BXlV` | `singleLineText` | Type: singleLineText |  |
| **LastTouchEventName**<br>`fldRxz3h7qcADlPMh` | `singleLineText` | Type: singleLineText |  |
| **DateTime**<br>`fldkwXuNh3Ylj2e07` | `dateTime` | Date and time |  |
| **SingleLineText**<br>`fldkDvbKwMaSeUrLX` | `singleLineText` | Type: singleLineText |  |
| **LastTouchPageURL**<br>`fldljNOB7DNSkg4uH` | `multilineText` | Multi-line text |  |

---

## 📋 21. KORU_Doors

*Table ID: `tblBzBO7U0loXWHfB`*
*Fields: 8*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **DoorID**<br>`fldIFUWfVadEdbByi` | `singleLineText` | Type: singleLineText |  |
| **DoorKey**<br>`fldg4D9mggyB2HZat` | `singleLineText` | Type: singleLineText |  |
| **DoorName**<br>`fldGs5R8avu975UUx` | `singleLineText` | Type: singleLineText |  |
| **DoorCategory**<br>`fldeg64i2jPNk0Bfi` | `singleLineText` | Type: singleLineText |  |
| **IsFreemiumAvailable**<br>`fld8ocjRszgoMEng2` | `checkbox` | True/False checkbox |  |
| **IsPremiumOnly**<br>`fld9GvNhdv6eRPsbe` | `checkbox` | True/False checkbox |  |
| **Status**<br>`fldj9N6dL6lTaJTjI` | `singleLineText` | Type: singleLineText |  |
| **StrategicRole**<br>`fldf8tPhQWXLBZiPc` | `multilineText` | Multi-line text |  |

---

## 📋 22. KORU_DoorUsage

*Table ID: `tblHp5f3aD3rLFGl6`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **DoorUsageID**<br>`fld5dTij09eVMSWjR` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fld6jCZ9ZkHrmVJUQ` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fld0GOazT7dYfcdbt` | `singleLineText` | Type: singleLineText |  |
| **SessionID**<br>`flds5nlBfXGVtQxld` | `singleLineText` | Type: singleLineText |  |
| **DoorKey**<br>`fldMbxEICFhTlBBDL` | `singleLineText` | Type: singleLineText |  |
| **StartedAt**<br>`fld68YVQtANseuQBs` | `dateTime` | Date and time |  |
| **CompletedAt**<br>`fldSUIUyNervHmDqs` | `dateTime` | Date and time |  |
| **DurationSeconds**<br>`fldR3ioCRIBuiU0Mp` | `number` | Numeric field |  |
| **MessageCount**<br>`fldfG20HumGF0cNL1` | `number` | Numeric field |  |
| **LearningWin**<br>`fldPDjAYVTvn7Drtk` | `checkbox` | True/False checkbox |  |
| **GapDetected**<br>`fldweyxyxfOO0M8rM` | `checkbox` | True/False checkbox |  |
| **GapWorked**<br>`fld4zxYwnrjCQvTZb` | `checkbox` | True/False checkbox |  |
| **UpgradeClicked**<br>`fldUiHkeQiBPkJuxB` | `checkbox` | True/False checkbox |  |
| **PlanAtUsage**<br>`fldXH4ha510DrbhCg` | `singleLineText` | Type: singleLineText |  |

---

## 📋 23. Leads

*Table ID: `tblJm5bEpjpYFOyXu`*
*Fields: 21*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Nombre**<br>`fldhinCyvJZ9OuYYM` | `singleLineText` | Type: singleLineText |  |
| **Mail**<br>`fld8Hbv3Aa7F5yd6Y` | `email` | Email address |  |
| **FechaCreacion**<br>`fldS8Gi4RsSNcjK6g` | `createdTime` | Auto-generated creation time |  |
| **FechaEnvioRegalo**<br>`fldQE0HJvZQRO49oy` | `dateTime` | Date and time |  |
| **FechaRetargeting24hrs**<br>`fldNvqo2MgTjKExGi` | `dateTime` | Date and time |  |
| **Pais**<br>`fldbnhH33vFPgt0xW` | `singleSelect` | Single choice dropdown | `AR`, `BO`, `BR`, `CL`, `CO` *(+5 more)* |
| **UTMSource**<br>`fld4TLED9yKFET97o` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldDoauIYuC1z68Gt` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldaSMb3Pu29FkLyN` | `singleLineText` | Type: singleLineText |  |
| **Compro**<br>`fldoa1D8FEjKxulex` | `checkbox` | True/False checkbox |  |
| **flagEnvioMail**<br>`fldKbuZDjbUyLsjf2` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldhinCyvJZ9OuYYM}!="",{fld8Hbv3...` |
| **Whatsapp**<br>`fld0955CrovA5rCtQ` | `phoneNumber` | Phone number |  |
| **FormatoPreferido**<br>`fldMTpyWwf6jGAtrf` | `singleLineText` | Type: singleLineText |  |
| **PrecioAceptable**<br>`fldLMQ3XnS3KiXOo1` | `singleLineText` | Type: singleLineText |  |
| **ProblemaMedioPago**<br>`flda6jhow5Vo8fTLt` | `multilineText` | Multi-line text |  |
| **InteresTaller**<br>`fldnFghOmpxnKnmGW` | `singleLineText` | Type: singleLineText |  |
| **OrigenLead**<br>`fldIO9TUnjMVjzmbV` | `singleSelect` | Single choice dropdown | `Libro`, `KORU`, `EIA`, `OF` |
| **EIA_SesionOrigen**<br>`fldqQd2QeZ8IzzHTy` | `singleLineText` | Type: singleLineText |  |
| **RolDeclarado**<br>`fldYOxbkhaCHu7Ctp` | `singleSelect` | Single choice dropdown | `estudiante`, `madre_padre_tutor`, `docente`, `estudios_superiores`, `otro` |
| **EIA_Sesiones**<br>`fldrYbi1cTMgTrb9M` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AceptaComunicaciones**<br>`fldKfQH8GNjPg9dPS` | `checkbox` | True/False checkbox |  |

---

## 📋 24. Logros

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

## 📋 25. Mensajes

*Table ID: `tblk3NUMOZhQX42AJ`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Mensaje**<br>`fldICiv65DcYl0ZMO` | `autoNumber` | Type: autoNumber |  |
| **Conversacion**<br>`fld0lhvJqLpoX8lzh` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiante**<br>`fldq4HaCjf56NmdNv` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Rol**<br>`fldrBWwu17uehpmwN` | `singleSelect` | Single choice dropdown | `estudiante`, `asistente`, `sistema` |
| **Contenido**<br>`fldskyjOSEa80QeoI` | `richText` | Rich text with formatting |  |
| **TokensInput**<br>`fldRT5Mct3fm4KNdS` | `number` | Numeric field |  |
| **TokensCacheados**<br>`fldpIXq8JPF2CFEhG` | `number` | Numeric field |  |
| **TokensOutput**<br>`fld2ssxNptWy6YTJ9` | `number` | Numeric field |  |
| **TokensUsados**<br>`fld7kXyt2mxu2jff8` | `number` | Numeric field |  |
| **CostoMensaje**<br>`fldSYiKZmNSUahvGN` | `number` | Numeric field |  |
| **ModeloIA**<br>`fld0hzK2Pf0nah5Uq` | `singleLineText` | Type: singleLineText |  |
| **Timestamp**<br>`fldrycW7y7bBFaLUy` | `createdTime` | Auto-generated creation time |  |
| **ContieneImagen**<br>`fld8ohAvc4OTu8d7K` | `checkbox` | True/False checkbox |  |
| **MetricasDiarias**<br>`fldPbYZ1ceJdydjrN` | `singleLineText` | Type: singleLineText |  |

---

## 📋 26. MetricasDiarias

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

## 📋 27. MetricasNEE

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

## 📋 28. Pagadores

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

## 📋 29. Pagos

*Table ID: `tbllGZKmZYWmRTZk1`*
*Fields: 19*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Pago**<br>`fldtamvOsSzchyolz` | `singleLineText` | Type: singleLineText |  |
| **RecID**<br>`fldUaPouRZQfsPsON` | `formula` | Calculated field | Formula: `RECORD_ID()` |
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
| **CreatedTime**<br>`fldAVVrwayHnDv6e3` | `createdTime` | Auto-generated creation time |  |

---

## 📋 30. ParametrosGenerales

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

## 📋 31. PlanesEstudio

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

## 📋 32. PostulacionesConvenios

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

## 📋 33. PremiumRetention

*Table ID: `tbl0t8LOyXP5FIqk8`*
*Fields: 33*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **PremiumRetentionID**<br>`fldg25kXosp0twoWd` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldnz2hdfHD4LaqBi` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fld92w5YGYSGEl8iQ` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldrG0D4V75ITNdkP` | `singleLineText` | Type: singleLineText |  |
| **PremiumStartDate**<br>`fldZ5qo2ETDtJE5js` | `dateTime` | Date and time |  |
| **CurrentPremiumStatus**<br>`fldJLdCGE4L7nBKlg` | `singleLineText` | Type: singleLineText |  |
| **CurrentRetentionStage**<br>`fldMgc6Qfg6yGYMVk` | `singleLineText` | Type: singleLineText |  |
| **PremiumStartedBeforeActivation**<br>`fld4pFaOkANNuCXXF` | `checkbox` | True/False checkbox |  |
| **PremiumActivationAfterPaymentDays**<br>`fldSJ5L89ukodF6AZ` | `number` | Numeric field |  |
| **DaysAsPremium**<br>`fld6fIjm8jYADO9Yb` | `number` | Numeric field |  |
| **PaymentsSucceeded**<br>`fldEuCo0AykTvdAuZ` | `number` | Numeric field |  |
| **PaymentsFailed**<br>`fldmkjYZ0Wcgq1cDc` | `number` | Numeric field |  |
| **RenewalsSucceeded**<br>`fldrUy31DoPCv6y5V` | `number` | Numeric field |  |
| **RenewalsFailed**<br>`fldtxwdPcb1AONCwj` | `number` | Numeric field |  |
| **LastPaymentDate**<br>`fldLvDeg0TJnnuZ0n` | `dateTime` | Date and time |  |
| **NextPaymentDate**<br>`fldEuoZjHpKuwrdbJ` | `dateTime` | Date and time |  |
| **ChurnDate**<br>`fldBfRwARiNqIcsFi` | `dateTime` | Date and time |  |
| **PremiumDaysToChurn**<br>`fldw8p7li7bpd2bmy` | `number` | Numeric field |  |
| **PremiumSessionsTotal**<br>`fld5GreFcji5ybgWD` | `number` | Numeric field |  |
| **PremiumActiveDaysTotal**<br>`fld68IAxOF6xDGlHj` | `number` | Numeric field |  |
| **PremiumSessionsPerWeekLifetime**<br>`fldYYTUA7f0tnNPn2` | `number` | Numeric field |  |
| **PremiumSessionsPerWeekLast30d**<br>`fldszOB2YDBCnyjPZ` | `number` | Numeric field |  |
| **PremiumSessionsPerWeekLast60d**<br>`fldUFSMCwvZGh3Wus` | `number` | Numeric field |  |
| **PremiumLast30dSessions**<br>`fldmXy7s64oJfacBH` | `number` | Numeric field |  |
| **PremiumLast60dSessions**<br>`flddmLzrqcnGcrBcL` | `number` | Numeric field |  |
| **PremiumLast90dSessions**<br>`fldlUkNVxIag3tcfJ` | `number` | Numeric field |  |
| **PremiumLearningWinsTotal**<br>`fld5pUEIPkNh9JgXw` | `number` | Numeric field |  |
| **PremiumLearningWinsLast30d**<br>`fldoDDFm70voTmY8L` | `number` | Numeric field |  |
| **PremiumDoorsUsedTotal**<br>`fldalUKtyrctVuzCe` | `number` | Numeric field |  |
| **PremiumMotherTouchpointsTotal**<br>`fldvR4RKzPvskskKG` | `number` | Numeric field |  |
| **ChurnRiskScore**<br>`fldvxdI3A1QSx48It` | `number` | Numeric field |  |
| **LTVAccrued**<br>`fldxnPXOy62d1G0HL` | `number` | Numeric field |  |
| **ExpectedLTV**<br>`fldFAuoYhjTjFnkHu` | `number` | Numeric field |  |

---

## 📋 34. Recordatorios

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

## 📋 35. RecursosDidacticos

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

## 📋 36. ReferralEdges

*Table ID: `tblYJ9diivi7eANvr`*
*Fields: 15*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ReferralEdgeID**<br>`fldQ3ZhcEiQHhKrxd` | `singleLineText` | Type: singleLineText |  |
| **FromPersonID**<br>`fld1FQBZUG82063Fh` | `singleLineText` | Type: singleLineText |  |
| **FromAnonID**<br>`fldQcQLk3EIiMCYVF` | `singleLineText` | Type: singleLineText |  |
| **ToPersonID**<br>`fldIzEndEBXuPkOwu` | `singleLineText` | Type: singleLineText |  |
| **ToAnonID**<br>`fldsbJODolh5Zq4ix` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldpRLfGEFVEzM8MN` | `singleLineText` | Type: singleLineText |  |
| **ParentShareLinkID**<br>`fldE9A6w5cMYv3Z5b` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fldQOkCsvpQLa8lPH` | `singleLineText` | Type: singleLineText |  |
| **Depth**<br>`fld2B9Et8wtP2PHJt` | `number` | Numeric field |  |
| **RelationshipDeclared**<br>`fld8R55iH9w7U8wDw` | `singleLineText` | Type: singleLineText |  |
| **Confidence**<br>`fldcNcDfNAQ6quyGx` | `singleLineText` | Type: singleLineText |  |
| **FirstSeenAt**<br>`fldxHqiqmks9sE8Ct` | `dateTime` | Date and time |  |
| **ConvertedToLead**<br>`fldwBchAO0W70y8MS` | `checkbox` | True/False checkbox |  |
| **ConvertedToFreemium**<br>`fldxHB7Hy5qMYQ7BW` | `checkbox` | True/False checkbox |  |
| **ConvertedToPremium**<br>`fldRqOzimq1WyNAP5` | `checkbox` | True/False checkbox |  |

---

## 📋 37. Segments

*Table ID: `tblFhJSTxNvYarU9c`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **SegmentID**<br>`fldoITOEWGBt50gHn` | `singleLineText` | Type: singleLineText |  |
| **SegmentKey**<br>`fldk8gpLrdyUHH2AD` | `singleLineText` | Type: singleLineText |  |
| **SegmentName**<br>`fld0GqCLXZ61e5pjk` | `singleLineText` | Type: singleLineText |  |
| **Description**<br>`fldKGIBasf9qs6ZTb` | `multilineText` | Multi-line text |  |
| **CriteriaJSON**<br>`fldKDXOTYra3WkBkT` | `multilineText` | Multi-line text |  |
| **LastCalculatedAt**<br>`fldUvu6qr0Jw0rHMr` | `dateTime` | Date and time |  |
| **UsersCount**<br>`fldqgkizbuFKhMou6` | `number` | Numeric field |  |
| **RecommendedAction**<br>`fld93cI8kP2DRPhNi` | `multilineText` | Multi-line text |  |
| **Destination**<br>`fldavrYOkBlcaqzG6` | `singleLineText` | Type: singleLineText |  |

---

## 📋 38. Seguimiento

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

## 📋 39. SenalesDeInteres

*Table ID: `tblrD0bpHujQVuLUU`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Senal**<br>`fldNB1rgAcRDKsoHI` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`flduMAAjAsWJSUl7v` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **TipoSenal**<br>`fldDl7kgM5GFSeAvr` | `singleLineText` | Type: singleLineText |  |
| **Detalle**<br>`fldZQVSzNbNQAea3o` | `singleLineText` | Type: singleLineText |  |
| **FechaSenal**<br>`fldqPogW9e2YZuq8f` | `createdTime` | Auto-generated creation time |  |
| **PlanAlMomento**<br>`fld38CkJvSopH544u` | `singleLineText` | Type: singleLineText |  |
| **ModalidadPremium**<br>`fld1dJRBEkipPc060` | `singleLineText` | Type: singleLineText |  |
| **Procesada**<br>`fldc18D1EJTELawxJ` | `checkbox` | True/False checkbox |  |
| **FechaProcesada**<br>`fldBAWRR0Y0ZF2yog` | `dateTime` | Date and time |  |

---

## 📋 40. SesionesEstudio

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

## 📋 41. ShareLinks

*Table ID: `tblf4PF6o9rkIgIef`*
*Fields: 21*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ShareLinkID**<br>`fldeigRQhL3dvWvn6` | `singleLineText` | Type: singleLineText |  |
| **ShareCode**<br>`fldKcWbKsSO4E3dE8` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fld0OZDFlOz59F5Xh` | `singleLineText` | Type: singleLineText |  |
| **CreatedByPersonID**<br>`fldgH3j0XOcbYhxQV` | `singleLineText` | Type: singleLineText |  |
| **CreatedByAnonID**<br>`fldE4rvHm4fz6C137` | `singleLineText` | Type: singleLineText |  |
| **CreatedByRole**<br>`fldlWQGMIuMYsQJ5t` | `singleLineText` | Type: singleLineText |  |
| **CreatedFromEventID**<br>`fldySQs9oqiIvhwS0` | `singleLineText` | Type: singleLineText |  |
| **RootTouchpointID**<br>`fldGAY3hpgy0bMdmO` | `singleLineText` | Type: singleLineText |  |
| **RootCampaignID**<br>`fldZ4OIMe4DLeB41h` | `singleLineText` | Type: singleLineText |  |
| **ParentShareLinkID**<br>`fldqGluIpAQlAj762` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fld0G5ARpyIXOWFZJ` | `singleLineText` | Type: singleLineText |  |
| **ShareDepth**<br>`fldkF8q6G6zZFzXwm` | `number` | Numeric field |  |
| **ShareChannel**<br>`flddAwHUg1TOCaWVs` | `singleLineText` | Type: singleLineText |  |
| **ShareIntent**<br>`fldegsSnlTu5PiUg6` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fld8clLKg02neDjds` | `dateTime` | Date and time |  |
| **Clicks**<br>`fldJhsxFEKjHAeMXs` | `number` | Numeric field |  |
| **UniqueClicks**<br>`fldpxqfgpYQXUz2NN` | `number` | Numeric field |  |
| **ConversionsToLead**<br>`fldInwinMUgNusEl8` | `number` | Numeric field |  |
| **ConversionsToEIA**<br>`fldehiYyLNUOvyA3t` | `number` | Numeric field |  |
| **ConversionsToFreemium**<br>`flduc1i8jVXxJP2MD` | `number` | Numeric field |  |
| **ConversionsToPremium**<br>`fldjpw1OngSo19geG` | `number` | Numeric field |  |

---

## 📋 42. Suscripciones

*Table ID: `tblowJOhwqRvVsWWc`*
*Fields: 37*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Suscripcion**<br>`fldn1n7fwUweCvo2i` | `autoNumber` | Type: autoNumber |  |
| **recID**<br>`fldAfedipCBeazgI9` | `formula` | Calculated field | Formula: `RECORD_ID()` |
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
| **CodigoBeca**<br>`fld5n5OnZgqupfNXg` | `singleLineText` | Type: singleLineText |  |
| **Estado**<br>`fldi8RIHJ0G746lAr` | `singleSelect` | Single choice dropdown | `activa`, `cancelada`, `pendiente_cancelacion`, `suspendida`, `vencida` |
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
| **ModifiedTime**<br>`fld1XD2ApGtFfpLUa` | `lastModifiedTime` | Auto-generated modification time |  |

---

## 📋 43. UserLifecycleWindows

*Table ID: `tbl1cYmlsEI1rABvF`*
*Fields: 36*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **WindowID**<br>`fldAFZhKm6jPSOUfP` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldzKIAxPxjmkBiap` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldQsJ93x0DcOMb2o` | `singleLineText` | Type: singleLineText |  |
| **WindowType**<br>`fldHWl5f1VwqoaQZ0` | `singleLineText` | Type: singleLineText |  |
| **WindowNumber**<br>`fldwGdQjbS0s5Ezxx` | `number` | Numeric field |  |
| **WindowStart**<br>`fldshOxj2N4z4FRFp` | `dateTime` | Date and time |  |
| **WindowEnd**<br>`fld1rdc1fiZwcvpr6` | `dateTime` | Date and time |  |
| **DaysFromSignupStart**<br>`fldRBTonTTEEEEOeO` | `number` | Numeric field |  |
| **DaysFromPremiumStart**<br>`fld66KOyctWUcf3QE` | `number` | Numeric field |  |
| **SessionsCount**<br>`fldWe4873J7DiBjms` | `number` | Numeric field |  |
| **CompletedSessionsCount**<br>`fldSHhm2biMmrKVQe` | `number` | Numeric field |  |
| **ActiveDaysCount**<br>`fldtvCMSfwt7eqFSC` | `number` | Numeric field |  |
| **AvgSessionsPerWeek**<br>`fldKBk7tEFXeFsW0U` | `number` | Numeric field |  |
| **AvgSessionDuration**<br>`fldXURP3D2SdM9CGj` | `number` | Numeric field |  |
| **TotalMessages**<br>`fldwCwrgdOHDBr9ry` | `number` | Numeric field |  |
| **LearningWinsCount**<br>`fldjvMb3CD4kvluRP` | `number` | Numeric field |  |
| **BrechasDetectedCount**<br>`fldkgHkY4Un3NPJvU` | `number` | Numeric field |  |
| **BrechasWorkedCount**<br>`fldhHZqamz4QXLwZe` | `number` | Numeric field |  |
| **DoorsUsedCount**<br>`fldyeWWO8Cbr2NYXm` | `number` | Numeric field |  |
| **DoorsUsedList**<br>`fldYzMtWb9Ua86BO4` | `multilineText` | Multi-line text |  |
| **FirstDoorUsed**<br>`fldJtMqJgfdTZoPw5` | `singleLineText` | Type: singleLineText |  |
| **MostUsedDoor**<br>`fldV2qOyQdoFUdpL0` | `singleLineText` | Type: singleLineText |  |
| **DoorSequence**<br>`fldQi1EPpfQjrbJjr` | `multilineText` | Multi-line text |  |
| **LockedDoorClicks**<br>`fldDq1S5FKNtUCmLH` | `number` | Numeric field |  |
| **EIAUsedCount**<br>`fldNPh21qSSjn2312` | `number` | Numeric field |  |
| **EIAScoreDeltaAvg**<br>`fld6lkkywkL4hXi5d` | `number` | Numeric field |  |
| **SharesTotalTimes**<br>`fldPapW89JCMgndae` | `number` | Numeric field |  |
| **SharesEiaTimes**<br>`fldsy3o2jkyB4oepd` | `number` | Numeric field |  |
| **SharesKoruTimes**<br>`fldmLWXOj5euaVZJP` | `number` | Numeric field |  |
| **ShareClicksGenerated**<br>`fldsSRb8MjfDfC2do` | `number` | Numeric field |  |
| **ReferralLeadsGenerated**<br>`fldpLDdijlCTTNMRs` | `number` | Numeric field |  |
| **ReferralFreemiumsGenerated**<br>`fldA7FPhgbFmIzOQA` | `number` | Numeric field |  |
| **MotherTouchpointsCount**<br>`fldoY3ZdPXO1Qwsuj` | `number` | Numeric field |  |
| **PremiumStatusAtWindowEnd**<br>`fldnlGSp6Nnv71Irq` | `singleLineText` | Type: singleLineText |  |
| **ConvertedDuringWindow**<br>`fldkxVMcoI1OolaVP` | `checkbox` | True/False checkbox |  |
| **ChurnedDuringWindow**<br>`fld6NGvsCU9sQOe4b` | `checkbox` | True/False checkbox |  |

---

## 📋 44. Testimonios

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

## 🔄 About This Documentation

### 📋 Source Information
- **Base**: Default (`default`)
- **Base ID**: `app9c8iiAYRGxxhtH`
- **Generated**: 2026-07-26 10:06:46

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
**Last sync**: 2026-07-26 10:06:46

---
*Documentation for Default base - Generated 2026-07-26 10:06:46*