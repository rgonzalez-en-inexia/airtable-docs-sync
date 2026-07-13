# 🗂️ Airtable Database Structure - Production

> **Last update**: 2026-07-13 13:40:59
> **Base**: prod (Production)
> **Auto-generated** - Do not edit manually

## 📊 Summary

- **Tables**: 53
- **Total fields**: 1440
- **Base ID**: `appr2x4VzE0OySqOu`

- **singleSelect fields**: 91
- **multipleSelects fields**: 8
- **number fields**: 268
- **date fields**: 28
- **formula fields**: 22

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

*Table ID: `tbl5bbz43RzV0gIuw`*
*Fields: 12*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Codigo**<br>`fldc023KTbWvp388d` | `singleLineText` | Type: singleLineText |  |
| **Asignado**<br>`fldy4a0P95GCEs2J9` | `checkbox` | True/False checkbox |  |
| **Quién**<br>`fldwvdomvHxsGmDKL` | `singleLineText` | Type: singleLineText |  |
| **Tipo**<br>`fld491EELlMUN0tK5` | `singleSelect` | Single choice dropdown | `BECA`, `Tester` |
| **UsosMaximos**<br>`fldWjZe1tw5S7yFY4` | `number` | Numeric field |  |
| **UsosActuales**<br>`fldqPfHifS9SOuibW` | `number` | Numeric field |  |
| **FechaExpiracion**<br>`flddi3exBjtChdfAP` | `date` | Date |  |
| **Activo**<br>`fldUCnFepR87O4JxS` | `checkbox` | True/False checkbox |  |
| **Descripcion**<br>`fldjsEwDbIa9kgSW6` | `singleLineText` | Type: singleLineText |  |
| **DescuentoPp**<br>`fldKBS5omqiMOMWSU` | `percent` | Percentage |  |
| **EnUso**<br>`fldIGJcZ8NkUKOspG` | `checkbox` | True/False checkbox |  |
| **FechaPrimerUso**<br>`flde7mkDLH7aRjdSw` | `dateTime` | Date and time |  |

---

## 📋 4. Conversaciones

*Table ID: `tblhw3b9VCVrJtDu1`*
*Fields: 33*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Conversacion**<br>`fldhpzpygAWASqIcm` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldsFM6LQCnmLIpev` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FechaAltaEstudiante**<br>`fldzwhZAcGxX19VAw` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **PlanActual**<br>`fldbgbDsg38T8NiC1` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **TipoPuerta**<br>`fldfGrwAFFXcL5jos` | `singleSelect` | Single choice dropdown | `aprender`, `preparar-evaluacion`, `estudiar`, `mejorar-habitos`, `prepararme-paes` |
| **Titulo**<br>`fldNkHyWabgfGAThi` | `singleLineText` | Type: singleLineText |  |
| **MateriaPrincipal**<br>`fld6eG16Hs7av0euL` | `singleLineText` | Type: singleLineText |  |
| **TipoNEE**<br>`fldx65y33zQeiXOsi` | `singleLineText` | Type: singleLineText |  |
| **CantidadMensajes**<br>`fldQFSerbNJRUagkv` | `count` | Type: count |  |
| **CantidadMensajesFinal**<br>`fldNlONZcXOGV6s2M` | `number` | Numeric field |  |
| **Tokens**<br>`fldtCm0VWw3wvkt0V` | `rollup` | Rollup from linked records |  |
| **TokensFinal**<br>`fldaYGwxvLqtSFKws` | `number` | Numeric field |  |
| **PctCacheHit**<br>`fldY1hwGOEA5DakIT` | `number` | Numeric field |  |
| **TokensCacheados**<br>`fld41NxRNU8glw1qu` | `rollup` | Rollup from linked records |  |
| **CostoAPI**<br>`fldvidJST7G3PhaTs` | `rollup` | Rollup from linked records |  |
| **CostoPromedioMensaje**<br>`fldxuCDhxTLqE6NbA` | `formula` | Calculated field | Formula: `({fldvidJST7G3PhaTs}/{fldQFSerbNJRUagkv})+0` |
| **Resumen**<br>`fldLJbxM83Q7BLBfZ` | `multilineText` | Multi-line text |  |
| **FechaInicio**<br>`fldUuqJjygGEcscrS` | `createdTime` | Auto-generated creation time |  |
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
| **SemanaISO**<br>`fldlio9jZ4QLw6NMv` | `singleLineText` | Type: singleLineText |  |
| **Mensajes copy**<br>`fldlX17UOCCe9cdBc` | `singleLineText` | Type: singleLineText |  |

---

## 📋 5. Curriculum

*Table ID: `tbld18R3UfqhagW4u`*
*Fields: 26*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **OA**<br>`fldrjQyvXRk6shh5j` | `multilineText` | Multi-line text |  |
| **NumeroReg**<br>`fld8fkhty8OMXYwNX` | `autoNumber` | Type: autoNumber |  |
| **OAnivel**<br>`fld2iZPfBxmNgBXA8` | `number` | Numeric field |  |
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
| **OAnivelTxt**<br>`fldqX7bbGHJFCSJb9` | `singleSelect` | Single choice dropdown | `5° Básico`, `6° Básico`, `7° Básico`, `8° Básico` |
| **OAantiguedad**<br>`fldgT3bnJbcwkUnBD` | `number` | Numeric field |  |
| **NivelEdadEstandar**<br>`fldVqCsOu3Wua13aK` | `formula` | Calculated field | Formula: `{fld2iZPfBxmNgBXA8}+6+0` |
| **OACodigoMineduc**<br>`fld4Oi0wYePfaXF4u` | `formula` | Calculated field | Formula: `SWITCH(
  {fldPPTulbJihy1UmV},
  "Ciencias", "CN...` |
| **OASearchText**<br>`fldNe4oEjtpficiXP` | `formula` | Calculated field | Formula: `LOWER(
  {fld4Oi0wYePfaXF4u} & " " &
  {fldPPTul...` |
| **OAGDCardResumen**<br>`fldiI17iekm70NCMJ` | `aiText` | Type: aiText |  |
| **OASearchKeywords**<br>`fldvRQqQCvMomhx47` | `aiText` | Type: aiText |  |
| **OAGDPreguntaDetonante**<br>`fldsyTDPpIhzOgvb4` | `aiText` | Type: aiText |  |
| **OAGDClase**<br>`fldsa8yaKhNdCysh6` | `aiText` | Type: aiText |  |
| **OAGDCasa**<br>`fldDbFSNZCxbzkC5h` | `aiText` | Type: aiText |  |
| **OAGDDetectivePrompt**<br>`fld9SXQxVNyuQ8p4m` | `aiText` | Type: aiText |  |
| **OAGDCriteriosDocente**<br>`fldeCVjp0xlaCSbIm` | `aiText` | Type: aiText |  |

---

## 📋 6. EIA_Eventos

*Table ID: `tblhnjssnyySMdZhT`*
*Fields: 20*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EventoKey**<br>`fldKA2Lqi52KQdkmP` | `autoNumber` | Type: autoNumber |  |
| **Evento**<br>`fldHyeMplqphYYZIX` | `singleLineText` | Type: singleLineText |  |
| **Timestamp**<br>`fldXxEumwqJJ7FjBE` | `createdTime` | Auto-generated creation time |  |
| **SessionUUID**<br>`fldpLn8dz0GFxvJGY` | `singleLineText` | Type: singleLineText |  |
| **MetadataJSON**<br>`fldT8tri1UDi2B9ap` | `multilineText` | Multi-line text |  |
| **UTMSource**<br>`fldmARHiktOTLWdGt` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldZ1KUZ4vvpqrlmu` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fld62aQ1DEdmjVH7f` | `singleLineText` | Type: singleLineText |  |
| **PaisDetectadoIP**<br>`fldzwctsKStuJMzUw` | `singleLineText` | Type: singleLineText |  |
| **RolDeclarado**<br>`fldJk6Jv4gjGQvfCm` | `singleLineText` | Type: singleLineText |  |
| **SiteVersion**<br>`fld43iPL566OLzRiy` | `singleLineText` | Type: singleLineText |  |
| **WorkerVersion**<br>`fldWIOxL7fpT0EEbC` | `singleLineText` | Type: singleLineText |  |
| **JourneyID**<br>`fldgEdm3eTsO0l1W2` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fld8lVar3r5Wx4hoL` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldgYAQXa7LONcsdY` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fldI88O8j8hHbXQSX` | `singleLineText` | Type: singleLineText |  |
| **AppVersion**<br>`fldL5wo9R7cmci5Jw` | `singleLineText` | Type: singleLineText |  |
| **Environment**<br>`fldkWcyMOGXp3luDS` | `singleLineText` | Type: singleLineText |  |
| **Sesion**<br>`fldXLgTCJt4detOUK` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Intento**<br>`fldgFg6Hh3QToAVfB` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 7. EIA_Intentos

*Table ID: `tbl6VgMSkKJBaNEqF`*
*Fields: 34*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **IntentoKey**<br>`fldZ4E4ftikzJuUDw` | `autoNumber` | Type: autoNumber |  |
| **NumeroIntento**<br>`fldPvJWimPtOU7Hb5` | `number` | Numeric field |  |
| **EsValido**<br>`fldsBMbWrA39CNezG` | `checkbox` | True/False checkbox |  |
| **MotivoInvalido**<br>`fldP2LesjuI2jFav7` | `singleLineText` | Type: singleLineText |  |
| **PromptUsuario**<br>`fldKM9E7PQjPzSohc` | `multilineText` | Multi-line text |  |
| **PromptHash**<br>`fldfR9utsvIONEh9x` | `singleLineText` | Type: singleLineText |  |
| **CriterioUsuario**<br>`fldSoEXPwmUWdLJq0` | `multilineText` | Multi-line text |  |
| **RespuestaIA**<br>`fldjmARpZkdo7KZRx` | `multilineText` | Multi-line text |  |
| **RespuestaFueLimitada**<br>`fldltlaYAfmxJXOAZ` | `checkbox` | True/False checkbox |  |
| **CriticaEIA**<br>`fldOCOdsy5IskUY7W` | `multilineText` | Multi-line text |  |
| **JSONCoach**<br>`fldLxThKfBxsrfGm5` | `multilineText` | Multi-line text |  |
| **ScoreTotal**<br>`flduiBjS5LpZdnvyq` | `number` | Numeric field |  |
| **KPI_Claridad**<br>`fld7J52Nhv6c2QyKj` | `number` | Numeric field |  |
| **KPI_Precision**<br>`fldPi5MwDcSH2fuXl` | `number` | Numeric field |  |
| **KPI_PensamientoPropio**<br>`fldNcj4eEf6HlZfcT` | `number` | Numeric field |  |
| **KPI_VerificacionCritica**<br>`fldgcImRJ3W58GEfA` | `number` | Numeric field |  |
| **KPI_CuidadoAcademico**<br>`fldSeJ923HZk1wPJ3` | `number` | Numeric field |  |
| **Riesgo**<br>`fld6GOpo0ET5ONIS0` | `singleSelect` | Single choice dropdown | `verde`, `amarillo`, `rojo`, `invalido`, `etico` |
| **Nivel**<br>`fld70Ljhi8WwE9yfv` | `singleSelect` | Single choice dropdown | `modo_copia`, `modo_ayuda`, `modo_aprendiz`, `modo_copiloto`, `modo_detective` |
| **ModeloRespuesta**<br>`fldtT8QIZ7rp3saPw` | `singleLineText` | Type: singleLineText |  |
| **ModeloCoach**<br>`fldWx3JGZIhTvAfKP` | `singleLineText` | Type: singleLineText |  |
| **TokensInputRespuesta**<br>`fldCBnIpnr9xJKLa2` | `number` | Numeric field |  |
| **TokensOutputRespuesta**<br>`fldWtKMmbdXZV8R3y` | `number` | Numeric field |  |
| **TokensInputCoach**<br>`fldQzv49B7URWigRW` | `number` | Numeric field |  |
| **TokensOutputCoach**<br>`fldvAsaBU4ndbGvQg` | `number` | Numeric field |  |
| **CostoEstimado**<br>`fldIZ9yAeoFMjFiqw` | `number` | Numeric field |  |
| **CreatedAt**<br>`fldC8jfWKSL1eQxf0` | `createdTime` | Auto-generated creation time |  |
| **ModeloClassifier**<br>`fld2UR4NKoHT2pXHq` | `singleLineText` | Type: singleLineText |  |
| **TokensInputClassifier**<br>`fldqptFNzQiAso1Uc` | `number` | Numeric field |  |
| **TokensOutputClassifier**<br>`fldW8UnyWlPPivaB8` | `number` | Numeric field |  |
| **SessionUUID**<br>`fldb0FPeIlKqtPMHv` | `singleLineText` | Type: singleLineText |  |
| **Sesion**<br>`fld7qRfoXZJcCV5Uf` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EIA_Eventos**<br>`flduuXfEbVkgeabtV` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **ID_IntentoEIA**<br>`fldpEeJlzHa7vaNjf` | `singleLineText` | Type: singleLineText |  |

---

## 📋 8. EIA_Sesiones

*Table ID: `tbly9Go8V8CcHMsn9`*
*Fields: 52*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_SesionEIA**<br>`flda9P5ZsvQX3dhmT` | `autoNumber` | Type: autoNumber |  |
| **AnonID**<br>`fldxeTl7bRGe720oP` | `singleLineText` | Type: singleLineText |  |
| **NombreCompleto**<br>`fldKY6xhoBcfpzOfo` | `singleLineText` | Type: singleLineText |  |
| **RolDeclarado**<br>`fldTihVZlTFdL1v1R` | `singleSelect` | Single choice dropdown | `estudiante`, `madre_padre_tutor`, `docente`, `estudios_superiores`, `otro` |
| **EmailGuardado**<br>`fld4V6cglAh4JIjQ7` | `email` | Email address |  |
| **EdadDeclarada**<br>`fldEH7nwiD9fGbpI8` | `number` | Numeric field |  |
| **FechaNacimiento**<br>`fldhu469mQKXmxwgV` | `date` | Date |  |
| **PaisDetectadoIP**<br>`fldw2fbwffvFbf2DL` | `singleLineText` | Type: singleLineText |  |
| **PaisElegido**<br>`fldpD97ShiCl8Xn0n` | `singleSelect` | Single choice dropdown | `Argentina`, `Bolivia`, `Chile`, `Colombia`, `Ecuador` *(+3 more)* |
| **IPHash**<br>`fldU7vAEmLaYRzF7Q` | `singleLineText` | Type: singleLineText |  |
| **UserAgentHash**<br>`fld0lL8JjXaEEFpmg` | `singleLineText` | Type: singleLineText |  |
| **RequiereConsentimientoParental**<br>`fldpXwDWmgpN4yCsP` | `checkbox` | True/False checkbox |  |
| **EstadoConsentimientoParental**<br>`fld7QhasKJHmmNdB0` | `singleSelect` | Single choice dropdown | `no_requerido`, `pendiente`, `otorgado`, `revocado` |
| **TutorNombre**<br>`fldOjzp3h4adi6oaq` | `singleLineText` | Type: singleLineText |  |
| **TutorEmail**<br>`fldvZuxGr9AeMAdB8` | `email` | Email address |  |
| **TutorRelacion**<br>`fldd9BWgmjzZ0vqrp` | `singleSelect` | Single choice dropdown | `Padre`, `Madre`, `Tutor Legal` |
| **ConsentimientoPrivacidad**<br>`fldgCNTmFzdALnzwh` | `checkbox` | True/False checkbox |  |
| **FechaConsentimiento**<br>`fldm4bSoANaa8PfHk` | `dateTime` | Date and time |  |
| **VersionConsentimientoPrivacidad**<br>`fldc6la8pIzBc91iI` | `singleLineText` | Type: singleLineText |  |
| **VersionConsentimientoTerminos**<br>`fld5qLQqJEWQcC0oT` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`flddHZQm9kO353T4S` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldrLAvwapV5QunKd` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldSkIZohDA7RmIJF` | `singleLineText` | Type: singleLineText |  |
| **Referrer**<br>`fldPSnpZvNpl227Xd` | `url` | URL link |  |
| **ShareIDOrigen**<br>`fldma1wzAVnZMPpz0` | `singleLineText` | Type: singleLineText |  |
| **IntentosValidos**<br>`fldUdqjnJ6fmDWyy7` | `number` | Numeric field |  |
| **ScoreInicial**<br>`fldPTfX2Q1PJcih6O` | `number` | Numeric field |  |
| **ScoreFinal**<br>`fldLe9BxjMSmWEq5I` | `number` | Numeric field |  |
| **NivelInicial**<br>`fldYorYv05YHjGWvt` | `singleSelect` | Single choice dropdown | `modo_copia`, `modo_ayuda`, `modo_aprendiz`, `modo_copiloto`, `modo_detective` |
| **NivelFinal**<br>`fldpGdIc9nlRoH5EX` | `singleSelect` | Single choice dropdown | `modo_copia`, `modo_ayuda`, `modo_aprendiz`, `modo_copiloto`, `modo_detective` |
| **RiesgoInicial**<br>`fldQQ80fAmgJkzB3p` | `singleSelect` | Single choice dropdown | `verde`, `amarillo`, `rojo`, `invalido` |
| **RiesgoFinal**<br>`fldrMBT5MysXLJgFo` | `singleSelect` | Single choice dropdown | `verde`, `amarillo`, `rojo`, `invalido` |
| **ModoDetectiveUsado**<br>`fldNxOP3z5N6VxYk8` | `checkbox` | True/False checkbox |  |
| **Completada**<br>`fld5dtd1dbeDPWsiF` | `checkbox` | True/False checkbox |  |
| **TipoCierre**<br>`fld56VcgOUKFcN8p6` | `singleSelect` | Single choice dropdown | `completada`, `abandono_datos`, `abandono_prompt`, `abandono_critica`, `limite` *(+2 more)* |
| **ClickWhatsApp**<br>`fld62VIrlEnX9ooUZ` | `checkbox` | True/False checkbox |  |
| **ClickKoruFreemium**<br>`fldoORoiEPYhKA6Vf` | `checkbox` | True/False checkbox |  |
| **FechaTermino**<br>`fldvN5JgUCimagg7w` | `dateTime` | Date and time |  |
| **DuracionSegundos**<br>`fldPAXKqcFM1nNokA` | `number` | Numeric field |  |
| **CostoTotalEstimado**<br>`fldOIccDvbVuzwikq` | `number` | Numeric field |  |
| **TokensInputTotal**<br>`fld4YuqEL4RlQJHPV` | `number` | Numeric field |  |
| **TokensOutputTotal**<br>`fldMysrtMI0PEYyTQ` | `number` | Numeric field |  |
| **ModeloCoachUltimo**<br>`fldUTlhv2dNdeKSde` | `singleLineText` | Type: singleLineText |  |
| **ModeloRespuestaUltimo**<br>`fldd2DAhMi3lFfrF0` | `singleLineText` | Type: singleLineText |  |
| **EIA_Intentos**<br>`fldY6iMyWKMu7w9fN` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EIA_Eventos**<br>`fldnhC5JzzmClANxQ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **EIA_Shares**<br>`fldJPiWzBpYh9jz4C` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Lead**<br>`fldsbHPUTpdqfjAdw` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiante**<br>`fldgHyLgFe1ot7fGj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FechaInicio**<br>`fldv4B79LMekqcZmh` | `createdTime` | Auto-generated creation time |  |
| **SessionUUID**<br>`fldzyGJzkeLbhSP0A` | `singleLineText` | Type: singleLineText |  |
| **RecordID**<br>`fldyLzHSuTdy0Mn1Q` | `formula` | Calculated field | Formula: `RECORD_ID()` |

---

## 📋 9. EIA_Shares

*Table ID: `tbl7MsWdVXEkjhfGz`*
*Fields: 11*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ShareID**<br>`fldd28BJlUNe8PJrh` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldK6j0DPgZiChhIt` | `createdTime` | Auto-generated creation time |  |
| **ID_ShareEIA**<br>`fldrq5FOO3PHCa7VR` | `singleLineText` | Type: singleLineText |  |
| **TipoShare**<br>`fldzA078kB0a1flIR` | `singleLineText` | Type: singleLineText |  |
| **URLGenerada**<br>`fldl1eWnID0EvxUvV` | `url` | URL link |  |
| **MensajeSugerido**<br>`fldGJGWP50ie743YV` | `multilineText` | Multi-line text |  |
| **Clicks**<br>`fldxqMlzIlL8sgj4m` | `number` | Numeric field |  |
| **RegistrosAtribuidos**<br>`fld39ByoN51I4PkbO` | `number` | Numeric field |  |
| **SesionesAtribuidas**<br>`fldVfTxn7CrEnGATE` | `number` | Numeric field |  |
| **UltimoClick**<br>`fldSMJUZjVk4RWsvr` | `dateTime` | Date and time |  |
| **SesionOrigen**<br>`fldYVycpYDMqAD7E4` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

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
*Fields: 125*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Estudiante**<br>`fldp7qIUatWYG2zw2` | `autoNumber` | Type: autoNumber |  |
| **createdTime**<br>`fldEltn2PBE8QGSVM` | `createdTime` | Auto-generated creation time |  |
| **Email**<br>`fldaPohMI9tlgDW4t` | `email` | Email address |  |
| **SacarDeDashboard**<br>`fldtLsUh1RVBhX3Kj` | `checkbox` | True/False checkbox |  |
| **UltimaActividad**<br>`fld00gaBZOkktKJYO` | `dateTime` | Date and time |  |
| **CantidadConversaciones**<br>`fldkF1lllYaBcR4Bl` | `formula` | Calculated field | Formula: `{fldJZJ0PotO13gABR}+{fldA3hx5Y8HUCQQxe}+{fldT3F5dU...` |
| **SesionActivaToken**<br>`fldeNdxf94vhx95qp` | `singleLineText` | Type: singleLineText |  |
| **Trigger1**<br>`fldIgPFMi7SkSiYXu` | `formula` | Calculated field | Formula: `IF(
  AND({fldDs68JQokh38DX6}!="",{fldaPohMI9tlgD...` |
| **SesionActivaDeviceId**<br>`fldYLUuvamWwFf1Xm` | `singleLineText` | Type: singleLineText |  |
| **Contrasena**<br>`fld2VACy7rMKduyLP` | `multilineText` | Multi-line text |  |
| **Rol**<br>`fld62uCAFaxkz5scC` | `singleSelect` | Single choice dropdown | `Estudiante`, `Apoderado`, `Admin` |
| **Nombre**<br>`fldDs68JQokh38DX6` | `singleLineText` | Type: singleLineText |  |
| **LlegoPor**<br>`fld51E4NaVZvq9upz` | `singleSelect` | Single choice dropdown | `Aviso en Facebook`, `Aviso en Instagram`, `ChatGPT u otra IA`, `Convenio con tu colegio`, `Google` *(+8 more)* |
| **QuienDecidio**<br>`fldocqWgnEkChM2nQ` | `singleSelect` | Single choice dropdown | `Yo`, `Mi padre-madre o tutor(a)` |
| **Genero**<br>`fldQ7uWbpXHadpSMA` | `singleSelect` | Single choice dropdown | `Hombre`, `Mujer`, `Otro`, `Prefiero no registrarlo` |
| **Estado**<br>`fldN9UGcBbKrtGPYD` | `singleSelect` | Single choice dropdown | `Activo`, `Bloqueado`, `suspendido` |
| **Pais**<br>`fldlqQYUn3GMAVXHW` | `formula` | Calculated field | Formula: `IF({fld4e4pFqnpODVbJB}="",
  SWITCH({fldl1SW9SPvQ...` |
| **PaisElegido**<br>`fld4e4pFqnpODVbJB` | `singleSelect` | Single choice dropdown | `Argentina`, `Bolivia`, `Chile`, `Colombia`, `Costa Rica` *(+13 more)* |
| **TZ**<br>`fldBKjR4g8qcF9JZV` | `formula` | Calculated field | Formula: `IF({fld4e4pFqnpODVbJB}!="",
  SWITCH(
    {fld4e...` |
| **CodigoPais**<br>`fldl1SW9SPvQcxIpY` | `formula` | Calculated field | Formula: `IF({fld4e4pFqnpODVbJB}!="",
  SWITCH({fld4e4pFqnp...` |
| **Celular**<br>`fldDJTv1TC3Dwr8b1` | `phoneNumber` | Phone number |  |
| **NombrePreferido**<br>`fldLdC48e8cV7Qn1f` | `singleLineText` | Type: singleLineText |  |
| **Curso**<br>`fldhlrRfO42asiEru` | `singleSelect` | Single choice dropdown | `7 Básico`, `8 Básico`, `1 Medio`, `2 Medio`, `3 Medio` *(+1 more)* |
| **EdadActual**<br>`fldqWWnlGSugEUugs` | `number` | Numeric field |  |
| **EstiloAprendizaje**<br>`fld0ckIVlh46CtbVb` | `singleSelect` | Single choice dropdown | `Visual`, `Auditivo`, `Kinestésico`, `Lectura/Escritura`, `No lo sé` |
| **MateriasFuertes**<br>`fldNhz8Feiohchzi1` | `singleSelect` | Single choice dropdown | `Matemáticas`, `Lenguaje`, `Ciencias`, `Historia`, `Economía` |
| **MateriasDebiles**<br>`fldH2m6C9msfoYLRn` | `singleSelect` | Single choice dropdown | `Lenguaje`, `Historia`, `Matemáticas`, `Ciencias`, `Economía` |
| **HaRepetido**<br>`fldZgc8D6koiQgda4` | `checkbox` | True/False checkbox |  |
| **TiposNEE**<br>`fld4uN4bHlLVEz3Mx` | `multipleSelects` | Multiple choice dropdown | `TDAH`, `Dislexia`, `TEA`, `Discalculia`, `Ninguno` *(+1 more)* |
| **RecibePIE**<br>`fldn3Sioto5nfisur` | `checkbox` | True/False checkbox |  |
| **NivelAnsiedad**<br>`fld5u3seaJi0JePIG` | `number` | Numeric field |  |
| **InteresesPersonales**<br>`fldykiNRSZPdeVHw6` | `multipleSelects` | Multiple choice dropdown | `Crear contenidos`, `Escuchar música`, `Jugar en el celular`, `Juntarme con amigos(as)`, `Leer` *(+8 more)* |
| **Idolo**<br>`fldlI8eMEZJCzBo7Y` | `singleLineText` | Type: singleLineText |  |
| **AspiracionFutura**<br>`fldlS5kKiRrjMMLuo` | `multilineText` | Multi-line text |  |
| **OnboardingCompletado**<br>`fld1peJxyAKgqLRg6` | `checkbox` | True/False checkbox |  |
| **FechaRegistro**<br>`fldvMB0YXrUFGNThv` | `dateTime` | Date and time |  |
| **DiasDesdeUltima**<br>`fldYd2NI4ued8FXc7` | `formula` | Calculated field | Formula: `DATETIME_DIFF(
     SET_TIMEZONE(NOW(), 'America/...` |
| **CantidadConversacionesExitosas**<br>`fldY1vwqXfZLzzn2W` | `count` | Type: count |  |
| **DiaPreferido**<br>`fldESkDeDmK7TybbX` | `formula` | Calculated field | Formula: `IF(AND({fldJZJ0PotO13gABR}>={fldA3hx5Y8HUCQQxe},{f...` |
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
| **ModalidadPremium**<br>`fldyFxnLf3QYEoYKj` | `singleSelect` | Single choice dropdown | `Pago_Normal`, `Pago_Campaña`, `Descuento_Grupal`, `Beca_Colegio`, `Beca_Personal` *(+1 more)* |
| **CampanaId**<br>`fldwWox9y7hTiykir` | `singleLineText` | Type: singleLineText |  |
| **TramoGrupal**<br>`fldqdmmP5SqdO9ex8` | `singleSelect` | Single choice dropdown | `T1`, `T2`, `T3` |
| **PrecioPagadoMensual**<br>`fldQacjN5GCulioWn` | `number` | Numeric field |  |
| **FechaPago**<br>`fldUL833KTrU6As0a` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **FechaProximoVencimiento**<br>`fldv97mLTiSL3s5yj` | `multipleLookupValues` | Type: multipleLookupValues |  |
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
| **ConfirmaEdad**<br>`flduUy3LxXTKr9SFw` | `checkbox` | True/False checkbox |  |
| **FechaConfirmaEdad**<br>`fldfeZ0wWjVxQFR5C` | `dateTime` | Date and time |  |
| **Anuncios**<br>`fldnbVzJLcx4NsUuj` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AnunciosVistos**<br>`fld3I3aEDwtqgz2W9` | `singleLineText` | Type: singleLineText |  |
| **Testimonios**<br>`fldWJEC7RMA6aNhEs` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **IDExternoPago**<br>`fldQxB8ES0c0UAKem` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **PlanActual**<br>`fldMrctNRhGeIfVvC` | `singleLineText` | Type: singleLineText |  |
| **FechaVencimientoPlan**<br>`fldfl0TSu0IqXEPSR` | `date` | Date |  |
| **FechaEliminacion**<br>`fld0fy4zuSWh7hM4r` | `date` | Date |  |
| **CantidadConversacionesTotales**<br>`fldzQcJY2bDgg2JXX` | `count` | Type: count |  |
| **PlanRiesgo**<br>`fldbf0ySCVeuJNmls` | `checkbox` | True/False checkbox |  |
| **AvatarURL**<br>`fldzT2N08WHtBCFCW` | `url` | URL link |  |
| **FechaNacimiento**<br>`fldRBUsLvXLujfeBV` | `date` | Date |  |
| **EIA_Sesiones**<br>`fld59IAgbRHVpGL0m` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **SeñalesDeInteres**<br>`fldBY6HtkJKi1czyw` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Moneda**<br>`fld1qkqYcUHc3FhQZ` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **CantidadConversacionesDeDias**<br>`fldl1xOAyyG36aLK9` | `formula` | Calculated field | Formula: `{fldJZJ0PotO13gABR}+{fldA3hx5Y8HUCQQxe}+{fldT3F5dU...` |
| **CostoConversaciones**<br>`fldhmExmamR4rxTEb` | `rollup` | Rollup from linked records |  |
| **CostoPromedioConversacion**<br>`fldxOAOMeS6Z0s8XC` | `formula` | Calculated field | Formula: `IF({fldl1xOAyyG36aLK9}>0,
  {fldhmExmamR4rxTEb}/{...` |
| **AlertaPais**<br>`fldcDktn3l3CkEYSR` | `formula` | Calculated field | Formula: `IF({fldl1SW9SPvQcxIpY}!={fldeSwPyE7ua5wtSb},"!","O...` |
| **ModifiedTime**<br>`fld5Nl6wMSgPAbMjp` | `lastModifiedTime` | Auto-generated modification time |  |

---

## 📋 12. EventosSignificativos

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

## 📋 13. Events

*Table ID: `tblZrRQ7pvDXFMNpl`*
*Fields: 39*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **EventID**<br>`fldlHm9cCZFHYMXog` | `singleLineText` | Type: singleLineText |  |
| **EventName**<br>`fldcsxecrVmd2XGNU` | `singleLineText` | Type: singleLineText |  |
| **EventTime**<br>`fldo7xFA7ynoOsD5c` | `dateTime` | Date and time |  |
| **ReceivedAt**<br>`fld7wQeYG6AkYvdlJ` | `dateTime` | Date and time |  |
| **Environment**<br>`fld8lzgMJPyWXd8r6` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fldqb5loA4C4iiFUz` | `singleLineText` | Type: singleLineText |  |
| **AnonID**<br>`fldreoJ2JnDuQ9vFm` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fld13zeAGd2alEpe2` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldWl8PqXkC9yVl9D` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldgrDRVjuoGePTBo` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldO2ZXFXBFUC9baL` | `singleLineText` | Type: singleLineText |  |
| **JourneyID**<br>`fldcSgaFEw2hyjDrV` | `singleLineText` | Type: singleLineText |  |
| **SessionID**<br>`fldZng12EIfb1bMiA` | `singleLineText` | Type: singleLineText |  |
| **TouchpointID**<br>`fld1YPSF6ijgVUdFm` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldNoSJztMRsqu7BI` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fldpXWWyXaP9nv1x8` | `singleLineText` | Type: singleLineText |  |
| **InstitutionID**<br>`fldJCAfFPRmCeNywa` | `singleLineText` | Type: singleLineText |  |
| **CohortID**<br>`fldVfedG3B9stKBYq` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`fldaKWXXoR1uTjZZ6` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldTCeCFOabWhsMIO` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fld59LrbXw0dzo6s3` | `singleLineText` | Type: singleLineText |  |
| **UTMContent**<br>`fldLzSeqITIN0e2by` | `singleLineText` | Type: singleLineText |  |
| **UTMTerm**<br>`fldVnrPKTkc4m2Fvs` | `singleLineText` | Type: singleLineText |  |
| **Fbclid**<br>`fldu4Xu07PhfPvByJ` | `singleLineText` | Type: singleLineText |  |
| **Referrer**<br>`fldVT8XOFQJUtrbGh` | `multilineText` | Multi-line text |  |
| **PageURL**<br>`fldEIKzMigomzWlcW` | `multilineText` | Multi-line text |  |
| **AppVersion**<br>`fldeWmJhg9Qxdv6uW` | `singleLineText` | Type: singleLineText |  |
| **WorkerVersion**<br>`fldfvq2oKOgRaBNXH` | `singleLineText` | Type: singleLineText |  |
| **PropertiesJSON**<br>`fldIBAenV1uAc10tH` | `multilineText` | Multi-line text |  |
| **IdempotencyKey**<br>`flddlj75VgtGoOMxE` | `singleLineText` | Type: singleLineText |  |
| **CountryDetected**<br>`fldTeAfaCt9nAkMjZ` | `singleLineText` | Type: singleLineText |  |
| **CountrySelected**<br>`fldTLmhsrW1xQ5nF5` | `singleLineText` | Type: singleLineText |  |
| **CountryForAnalysis**<br>`fldSWzlIJqLbnwD5k` | `singleLineText` | Type: singleLineText |  |
| **RootJourneyID**<br>`fld32a19ljLCcpTJg` | `singleLineText` | Type: singleLineText |  |
| **ParentJourneyID**<br>`fldWJAoubgysEFs0Y` | `singleLineText` | Type: singleLineText |  |
| **ReferralID**<br>`fldRy1e9WjMqz2LsS` | `singleLineText` | Type: singleLineText |  |
| **Gclid**<br>`fld4kACIDNfM40cDr` | `singleLineText` | Type: singleLineText |  |
| **EventSource**<br>`fldGLPRPvqR4HMKj9` | `singleLineText` | Type: singleLineText |  |
| **SchemaVersion**<br>`fldTmTmxEBxCcEliw` | `singleLineText` | Type: singleLineText |  |

---

## 📋 14. GI_Ads

*Table ID: `tblm9wZRQmsYFwla7`*
*Fields: 34*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **AdKey**<br>`fldLNEzA0oYcnq5qx` | `singleLineText` | Type: singleLineText |  |
| **MetaAdID**<br>`fldzMg1rP9DGdmDlL` | `singleLineText` | Type: singleLineText |  |
| **MetaAdSetID**<br>`fldQB81t1VWYjA9Vg` | `singleLineText` | Type: singleLineText |  |
| **MetaCampaignID**<br>`fldlgmPa2HBuzetBa` | `singleLineText` | Type: singleLineText |  |
| **AdNameCurrent**<br>`fldyzu9nY5y9EEapn` | `singleLineText` | Type: singleLineText |  |
| **AdNameInitial**<br>`fldNxs0AW9ES7oNG9` | `singleLineText` | Type: singleLineText |  |
| **AdNameNormalized**<br>`fld7K0J2mynNkPFyg` | `singleLineText` | Type: singleLineText |  |
| **NameChanged**<br>`fldZfYL819XLgcviD` | `checkbox` | True/False checkbox |  |
| **MetaCreativeID**<br>`fldrzP5t7Abs8Lnp5` | `singleLineText` | Type: singleLineText |  |
| **CreativeConceptKey**<br>`fldjS8Pa1xA5OoQJc` | `singleLineText` | Type: singleLineText |  |
| **CreativeConceptName**<br>`fldOadIycGh5LahUF` | `singleLineText` | Type: singleLineText |  |
| **CreativeFormat**<br>`flddsHTZylSjt7HZ2` | `singleLineText` | Type: singleLineText |  |
| **CreativeAngle**<br>`fld2zmiwsrp5E1Lnz` | `singleLineText` | Type: singleLineText |  |
| **CreativeVersion**<br>`fldIU02tOVvGjwNtm` | `singleLineText` | Type: singleLineText |  |
| **CTAType**<br>`fldg2UijFcvQeRjoP` | `singleLineText` | Type: singleLineText |  |
| **DestinationURL**<br>`fldxypvi99fQNIyWI` | `url` | URL link |  |
| **UTMSourceExpected**<br>`fldn8xF60JtvqDLFz` | `singleLineText` | Type: singleLineText |  |
| **UTMMediumExpected**<br>`fldvcP9qq0TZH0JRB` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaignExpected**<br>`fldfBdN6GjeejI60f` | `singleLineText` | Type: singleLineText |  |
| **UTMTermExpected**<br>`fldj6wcToNhStCk6L` | `singleLineText` | Type: singleLineText |  |
| **UTMContentExpected**<br>`fld5AUxdWkQ4PpgaS` | `singleLineText` | Type: singleLineText |  |
| **Status**<br>`fldvGV6A5NFzECjgw` | `singleLineText` | Type: singleLineText |  |
| **EffectiveStatus**<br>`fldXwFx0gajEpLJpJ` | `singleLineText` | Type: singleLineText |  |
| **FirstActiveAt**<br>`fldCaZ0UVFqrfuxZB` | `dateTime` | Date and time |  |
| **LastActiveAt**<br>`fldCC6PHiEWyiG2sV` | `dateTime` | Date and time |  |
| **CreatedTimeMeta**<br>`fldWNObblzPf8hBeX` | `dateTime` | Date and time |  |
| **ConfigHashCurrent**<br>`fld4dFc4kh2euFCX6` | `singleLineText` | Type: singleLineText |  |
| **ConfigChanged**<br>`fldZ9fVg0aFip5Z3A` | `checkbox` | True/False checkbox |  |
| **LastSyncedAt**<br>`fldCPmSFmN8OqeuFm` | `dateTime` | Date and time |  |
| **Notes**<br>`fldvVEDWGOANuFR1k` | `multilineText` | Multi-line text |  |
| **SchemaVersion**<br>`fldNOkyHuPUGVippK` | `singleLineText` | Type: singleLineText |  |
| **GI_MetaAdsDaily**<br>`flddM7vDpaRVOmdcD` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_FunnelDaily**<br>`fld9JryIfAtky9FCt` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MarketingPerformanceDaily**<br>`fldyLSjSweeU3WefT` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 15. GI_AdSets

*Table ID: `tblGFOFFyOfPwo0zu`*
*Fields: 64*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **AdSetKey**<br>`fldc1CMsH0K4ilFT2` | `singleLineText` | Type: singleLineText |  |
| **MetaAdSetID**<br>`fld3CAfY3rlg4XrJU` | `singleLineText` | Type: singleLineText |  |
| **MetaCampaignID**<br>`fld2Tqg8Fk61qLP9D` | `singleLineText` | Type: singleLineText |  |
| **AdSetNameCurrent**<br>`fldn8jj5tXjznXJCa` | `singleLineText` | Type: singleLineText |  |
| **AdSetNameInitial**<br>`fldstT3GtrKNOhU56` | `singleLineText` | Type: singleLineText |  |
| **AdSetNameNormalized**<br>`fldHldnhjYdI0V09a` | `singleLineText` | Type: singleLineText |  |
| **NameChanged**<br>`fldPHZq8spythCf6s` | `checkbox` | True/False checkbox |  |
| **Status**<br>`fldZnFbiW0mDxjInN` | `singleLineText` | Type: singleLineText |  |
| **EffectiveStatus**<br>`fldFJflz5oQ7RCTbJ` | `singleLineText` | Type: singleLineText |  |
| **CreatedTimeMeta**<br>`fldqnEq0iEXS0YBX6` | `dateTime` | Date and time |  |
| **StartTimeMeta**<br>`fldqfxz03beYdXN5q` | `dateTime` | Date and time |  |
| **EndTimeMeta**<br>`fldRGmTIAE2hl1WVu` | `dateTime` | Date and time |  |
| **LastSyncedAt**<br>`fldkaUULOdfepUWVT` | `dateTime` | Date and time |  |
| **TargetRole**<br>`fld1oF44o1utaKlOc` | `singleLineText` | Type: singleLineText |  |
| **AgeMin**<br>`flduNTYBzYJbUaAAd` | `number` | Numeric field |  |
| **AgeMax**<br>`fldRPiw1EcTZnil09` | `number` | Numeric field |  |
| **SocioeconomicSegment**<br>`fldfNTPYUoLzBaSTg` | `singleLineText` | Type: singleLineText |  |
| **SegmentDefinition**<br>`fld1tQUH1uZXlunKc` | `multilineText` | Multi-line text |  |
| **TargetCountryPrimary**<br>`fldWhH3eC6kUUvs1R` | `singleLineText` | Type: singleLineText |  |
| **TargetCountryCodesJSON**<br>`fld61caoeR9ynlGzE` | `multilineText` | Multi-line text |  |
| **GeoKey**<br>`fldOLVTRWhrYEfazI` | `singleLineText` | Type: singleLineText |  |
| **GeoLabel**<br>`fld749N5p8cSeAA4n` | `singleLineText` | Type: singleLineText |  |
| **GeoScopeType**<br>`fldsVcvzrE8qRjhYt` | `singleLineText` | Type: singleLineText |  |
| **GeoTargetsJSON**<br>`fldsYQaXcAOeNr8TN` | `multilineText` | Multi-line text |  |
| **GeoExclusionsJSON**<br>`fldEa8AMj93htlFFs` | `multilineText` | Multi-line text |  |
| **TargetingJSON**<br>`fld5l0rysnQuYsNJe` | `multilineText` | Multi-line text |  |
| **LanguagesJSON**<br>`fldIMKBLhocGLYUaq` | `multilineText` | Multi-line text |  |
| **PlacementsMode**<br>`fldbtTdnnYowrlfv8` | `singleLineText` | Type: singleLineText |  |
| **PlacementsJSON**<br>`fldyM83NGjiY6NDH9` | `multilineText` | Multi-line text |  |
| **OptimizationGoal**<br>`fldgi7ytNIxAXjhAf` | `singleLineText` | Type: singleLineText |  |
| **OptimizationEventMeta**<br>`fldDC5uuv9c1nYGZV` | `singleLineText` | Type: singleLineText |  |
| **OptimizationEventGIEquivalent**<br>`fldqZHP8a5juwowum` | `singleLineText` | Type: singleLineText |  |
| **BillingEvent**<br>`fldMyrXPdr3lzV8FJ` | `singleLineText` | Type: singleLineText |  |
| **BidStrategy**<br>`fldhe6Ai1ZhQHv0x3` | `singleLineText` | Type: singleLineText |  |
| **AttributionSetting**<br>`fldkTxbvBCQBx1Dap` | `singleLineText` | Type: singleLineText |  |
| **PromotedObjectJSON**<br>`fldgyIjGyvOcEQvDb` | `multilineText` | Multi-line text |  |
| **BudgetSource**<br>`fldzaTkVYd9AWUXak` | `singleLineText` | Type: singleLineText |  |
| **BudgetType**<br>`fldp3Hv3Ki9iZnnYx` | `singleLineText` | Type: singleLineText |  |
| **CurrentBudgetAccountCurrency**<br>`fld6pyx1c2ZO52Nsv` | `number` | Numeric field |  |
| **AccountCurrencyCode**<br>`fld0I4onTVIMBlxUC` | `singleLineText` | Type: singleLineText |  |
| **LearningStatus**<br>`fldK16pGQ8R4jFShN` | `singleLineText` | Type: singleLineText |  |
| **AudiencePotentialLowerCurrent**<br>`fldDNrW0kqB80L2cp` | `number` | Numeric field |  |
| **AudiencePotentialUpperCurrent**<br>`fldrgLnPScjVpOits` | `number` | Numeric field |  |
| **AudiencePotentialMidpointCurrent**<br>`fldKqhY5D7A0dOqtC` | `number` | Numeric field |  |
| **AudienceEstimateCapturedAt**<br>`fldcMvTYz6efm6Ehv` | `dateTime` | Date and time |  |
| **AudienceEstimateStatus**<br>`fldw9fwanUJPAhaqM` | `singleLineText` | Type: singleLineText |  |
| **AudienceEstimateConfigHash**<br>`fld3LEaGcM3KNFu49` | `singleLineText` | Type: singleLineText |  |
| **AudienceEstimateError**<br>`fld5GyFb5r2wJgLgQ` | `multilineText` | Multi-line text |  |
| **ConfigHashCurrent**<br>`fldsqTNzltJmY1gcD` | `singleLineText` | Type: singleLineText |  |
| **ConfigHashPrevious**<br>`fld3VqYsnoXbC0jcZ` | `singleLineText` | Type: singleLineText |  |
| **ConfigChanged**<br>`fldRd9E36oC5FmXuc` | `checkbox` | True/False checkbox |  |
| **LastConfigChangeAt**<br>`fldYZDcVgmuNhVRi3` | `dateTime` | Date and time |  |
| **LastConfigChangeType**<br>`fld7NzDpwYwyN5eb7` | `singleLineText` | Type: singleLineText |  |
| **AnalysisContinuityBroken**<br>`fld7skh3V8WDdbifN` | `checkbox` | True/False checkbox |  |
| **ContinuityBreakReason**<br>`fldh5vJx5xIwjFgsI` | `multilineText` | Multi-line text |  |
| **Notes**<br>`fldWOZwm25rHeK4OD` | `multilineText` | Multi-line text |  |
| **SchemaVersion**<br>`fldpHGIiclaQCwZho` | `singleLineText` | Type: singleLineText |  |
| **Campaign**<br>`fldC15eCqsIPHHkgs` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Geography**<br>`fldrF3Yf2q5lMQxkR` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_AdSetConfigSnapshots**<br>`fld1Iu9YexSO6PUzi` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MetaAdsDaily**<br>`fldtnBvoUg87IKk9M` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MetaAudienceSnapshots**<br>`fld1zV5rf1KD6hine` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_FunnelDaily**<br>`fldwbxFPPUcoaohUr` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MarketingPerformanceDaily**<br>`fld6upAa7szZJkIr1` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 16. GI_Campaigns

*Table ID: `tbllsjg8Ps1H4ggrB`*
*Fields: 39*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **CampaignKey**<br>`fldKXVxNNMQW28h7F` | `singleLineText` | Type: singleLineText |  |
| **MetaAccountID**<br>`fld6lxVQvY4bQoV5n` | `singleLineText` | Type: singleLineText |  |
| **MetaCampaignID**<br>`fldm4GUGVCmCOqfMX` | `singleLineText` | Type: singleLineText |  |
| **CampaignNameCurrent**<br>`fldtiiuDaONDxBgt6` | `singleLineText` | Type: singleLineText |  |
| **CampaignNameInitial**<br>`fldUO298FUjouD49k` | `singleLineText` | Type: singleLineText |  |
| **CampaignNameNormalized**<br>`fldCb4MqOEYsPStGl` | `singleLineText` | Type: singleLineText |  |
| **NameChanged**<br>`fldeE7Ef8i6WEBarX` | `checkbox` | True/False checkbox |  |
| **Status**<br>`fldvzExJaXFYG5QoA` | `singleLineText` | Type: singleLineText |  |
| **EffectiveStatus**<br>`fldaEuMCDKzXyDkQa` | `singleLineText` | Type: singleLineText |  |
| **MetaObjective**<br>`fldSMi3rpdBMEUpSR` | `singleLineText` | Type: singleLineText |  |
| **BuyingType**<br>`fldq7cuG13CEmjomU` | `singleLineText` | Type: singleLineText |  |
| **CreatedTimeMeta**<br>`fld6dRjxres7sHlI4` | `dateTime` | Date and time |  |
| **StartDate**<br>`fldYK0FeZeSxfxGWC` | `date` | Date |  |
| **EndDate**<br>`fldMXFJEwHL3sfcIJ` | `date` | Date |  |
| **LastSyncedAt**<br>`fldntHFl0QxKdzXUF` | `dateTime` | Date and time |  |
| **CountryStrategy**<br>`flde15ibihbRcukwo` | `singleLineText` | Type: singleLineText |  |
| **FunnelStage**<br>`fldvTHBL9Rai6ejiu` | `singleLineText` | Type: singleLineText |  |
| **StrategicObjective**<br>`fldTVPIwu9zKhFdyu` | `multilineText` | Multi-line text |  |
| **PrimaryGIMetric**<br>`fldma7X53FKgi5sR4` | `singleLineText` | Type: singleLineText |  |
| **SecondaryGIMetrics**<br>`fldWP849pKbdLcWbX` | `multilineText` | Multi-line text |  |
| **Hypothesis**<br>`fldaa2aPTWsUHhYq0` | `multilineText` | Multi-line text |  |
| **ScaleCriteria**<br>`fldSg8Dcf2N8BqANt` | `multilineText` | Multi-line text |  |
| **PauseCriteria**<br>`fldWJzRXzj6V6A4qu` | `multilineText` | Multi-line text |  |
| **DecisionStatus**<br>`fldxgpQ1gaCZAd2t0` | `singleLineText` | Type: singleLineText |  |
| **DecisionRationale**<br>`fldoETIHnhO2rVFqX` | `multilineText` | Multi-line text |  |
| **Owner**<br>`fldn6Rpplgu7rIh4i` | `singleLineText` | Type: singleLineText |  |
| **Notes**<br>`fldWzOznGAqslGAXy` | `multilineText` | Multi-line text |  |
| **BudgetLevel**<br>`fld5xBanHCTu9Uwzi` | `singleLineText` | Type: singleLineText |  |
| **BudgetType**<br>`fldHyHOD02HFySCA0` | `singleLineText` | Type: singleLineText |  |
| **CurrentBudgetAccountCurrency**<br>`fldfRE9FDYbq3zP98` | `number` | Numeric field |  |
| **AccountCurrencyCode**<br>`fld0yxRoLwZCEGE1t` | `singleLineText` | Type: singleLineText |  |
| **SpendCapAccountCurrency**<br>`fldyHYYZ0aGpwNpPY` | `number` | Numeric field |  |
| **SchemaVersion**<br>`fldeU26pmGQV2zwpm` | `singleLineText` | Type: singleLineText |  |
| **GI_AdSets**<br>`fld56a8EcehRsKZnR` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_AdSetConfigSnapshots**<br>`fld6OR54P2w0NVuTD` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MetaAdsDaily**<br>`fldbcM6QAypgxPsB9` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MetaAudienceSnapshots**<br>`fldQKwFPmRKwDqYVl` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_FunnelDaily**<br>`fld6LAkofiVWAO5DT` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **GI_MarketingPerformanceDaily**<br>`fldYCSBjmEPGK8Tcg` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 17. GI_FunnelDaily

*Table ID: `tblJ9KrYI5GIhkCHh`*
*Fields: 67*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **FunnelDailyKey**<br>`fldO0aRrpUe7WNUyc` | `singleLineText` | Type: singleLineText |  |
| **Date**<br>`fldaE2lerC5TeqIWF` | `date` | Date |  |
| **Environment**<br>`fldBTgzVhqrz3PnT9` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`fldVMYyBZ3kDAjjdA` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldxc4YE6A0CZcQ4D` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldAQUZxscopQ19M1` | `singleLineText` | Type: singleLineText |  |
| **UTMTerm**<br>`fldhZ4DMoTsMZgfTt` | `singleLineText` | Type: singleLineText |  |
| **UTMContent**<br>`fldfXIy6fO6zVADQJ` | `singleLineText` | Type: singleLineText |  |
| **MetaCampaignIDResolved**<br>`fldFpAmnE4GawrqfH` | `singleLineText` | Type: singleLineText |  |
| **MetaAdSetIDResolved**<br>`fldqmg0HJMVMP2YWP` | `singleLineText` | Type: singleLineText |  |
| **MetaAdIDResolved**<br>`fld5p7XqETtuQZiUG` | `singleLineText` | Type: singleLineText |  |
| **TargetCountryCode**<br>`fldFx8klD85Co7LYR` | `singleLineText` | Type: singleLineText |  |
| **GeoKey**<br>`fld1scCItJrOX2q8g` | `singleLineText` | Type: singleLineText |  |
| **SocioeconomicSegment**<br>`fldHYv9oUeqBB73v9` | `singleLineText` | Type: singleLineText |  |
| **TargetRole**<br>`fldixv299XAblQsm5` | `singleLineText` | Type: singleLineText |  |
| **ProductPath**<br>`fldW2MPhsEATjOQNp` | `singleLineText` | Type: singleLineText |  |
| **EventsTotal**<br>`fldFWWClpTHqIt8PP` | `number` | Numeric field |  |
| **UniqueJourneys**<br>`fld9OtSj4TYFVzISb` | `number` | Numeric field |  |
| **UniqueRootJourneys**<br>`fld6snQtwJRkg9SWS` | `number` | Numeric field |  |
| **UniqueAnonymousUsers**<br>`fldCeD9slRdGknC9f` | `number` | Numeric field |  |
| **UniqueStudents**<br>`fldc7I93HdokN964l` | `number` | Numeric field |  |
| **EventsWithoutJourneyID**<br>`fldOBIRs7CvnSgxdZ` | `number` | Numeric field |  |
| **EventsWithoutCompleteUTM**<br>`fldwoWoTWnTtgCSLa` | `number` | Numeric field |  |
| **EventsWithoutResolvedAd**<br>`fldBUuO72ME2ORIU7` | `number` | Numeric field |  |
| **AttributionCoveragePct**<br>`fldSfUEuOY6w6ZVW5` | `percent` | Percentage |  |
| **CountryMismatchEvents**<br>`fldavriMg4RLn3jKI` | `number` | Numeric field |  |
| **KoruLandingViewed**<br>`fldg3iJc50BhO5xtY` | `number` | Numeric field |  |
| **KoruQualifiedVisit**<br>`fldpPDkOvSx2NB6JG` | `number` | Numeric field |  |
| **KoruCtaClicked**<br>`fldYrL3BEZIbLA9zz` | `number` | Numeric field |  |
| **KoruShareCreated**<br>`fldnjNfguGAtxL8yp` | `number` | Numeric field |  |
| **KoruShareToChildCreated**<br>`fldOg8owVqiD75bZ5` | `number` | Numeric field |  |
| **EiaLandingViewed**<br>`fldTBxN3A8XrytF8o` | `number` | Numeric field |  |
| **EiaQualifiedVisit**<br>`fldN7A0WxqYhCccR0` | `number` | Numeric field |  |
| **EiaModeSelected**<br>`fldSHMS3ix4TPBRUY` | `number` | Numeric field |  |
| **EiaSessionStarted**<br>`fldIxmF74Sc7IQAYn` | `number` | Numeric field |  |
| **EiaSessionCompleted**<br>`fldUosHboTloEA1jJ` | `number` | Numeric field |  |
| **EiaTrainingSaved**<br>`fldsEPPlgVn3r74cd` | `number` | Numeric field |  |
| **EiaKoruCtaClicked**<br>`fldM3x00mDu8pNArk` | `number` | Numeric field |  |
| **EiaShareCreated**<br>`fldf7PCV9Adpol54u` | `number` | Numeric field |  |
| **EiaShareToChildCreated**<br>`fldwD9zOUlwHXjxGL` | `number` | Numeric field |  |
| **EiaDetectiveStarted**<br>`fld9A8wC9GNizE2sJ` | `number` | Numeric field |  |
| **EiaDetectiveEvaluated**<br>`fldGYdvHALcP3toIh` | `number` | Numeric field |  |
| **KoruSignupStarted**<br>`fldEWZEx4VRHFZYVK` | `number` | Numeric field |  |
| **KoruFreemiumRegistered**<br>`fldblQQC50B6vZIN3` | `number` | Numeric field |  |
| **KoruFirstSessionStarted**<br>`fldBdbm0a4SkxzzJS` | `number` | Numeric field |  |
| **KoruFirstSessionCompleted**<br>`fldglKvZRMV8yGuPw` | `number` | Numeric field |  |
| **KoruSecondSessionCompleted**<br>`fld8l1hvO7c1vFYcy` | `number` | Numeric field |  |
| **KoruActivationAchieved**<br>`fld9bigN0KnWPjlwE` | `number` | Numeric field |  |
| **PremiumOfferViewed**<br>`fldiB75PPflZ3BgT9` | `number` | Numeric field |  |
| **PremiumCheckoutStarted**<br>`fldt7vv9lJFoTZATO` | `number` | Numeric field |  |
| **PremiumPaymentCompleted**<br>`fldqvGS0c0YSoDykh` | `number` | Numeric field |  |
| **PremiumStarted**<br>`fldPFjRFcmqFjJfe0` | `number` | Numeric field |  |
| **PremiumRetained30d**<br>`fldogBVSIqJYBDE7G` | `number` | Numeric field |  |
| **PremiumRetained90d**<br>`fldwz61iD9CGlZwzi` | `number` | Numeric field |  |
| **ShareLinksOpened**<br>`fldAuDEYPF09Bk8T4` | `number` | Numeric field |  |
| **ReferralSessionsStarted**<br>`fldvngYR26BN8D380` | `number` | Numeric field |  |
| **ReferralFreemiumRegistered**<br>`fldYJt76V6Vgcj72S` | `number` | Numeric field |  |
| **ReferralPremiumStarted**<br>`fld3DKy8UXn35vHkb` | `number` | Numeric field |  |
| **CalculatedAt**<br>`fldkZgG7sQAtl7CmF` | `dateTime` | Date and time |  |
| **AggregationVersion**<br>`fldcedA6PAnkLvwy3` | `singleLineText` | Type: singleLineText |  |
| **CalculationRunID**<br>`fldS4eMqfkJ5B3dLw` | `singleLineText` | Type: singleLineText |  |
| **CalculationStatus**<br>`fldIVgT5bTxndOVML` | `singleLineText` | Type: singleLineText |  |
| **CalculationWarnings**<br>`fldoYMFVzkyUu4WTB` | `multilineText` | Multi-line text |  |
| **SchemaVersion**<br>`fldYR7lajt7eFQohX` | `singleLineText` | Type: singleLineText |  |
| **Campaign**<br>`fldvdCvU78EcNqJSa` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AdSet**<br>`fld4EaAr91XlbFbTU` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Ad**<br>`fldDOO2CeaxCJjAhY` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 18. GI_AdSetConfigSnapshots

*Table ID: `tbljLiNtIkEmfWyVu`*
*Fields: 31*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ConfigSnapshotKey**<br>`flduA1M40zzZYZXDF` | `singleLineText` | Type: singleLineText |  |
| **SnapshotAt**<br>`fldDchBZXQWYFgPwI` | `dateTime` | Date and time |  |
| **SnapshotDate**<br>`fldOrcz78U13UOZi3` | `date` | Date |  |
| **MetaAdSetID**<br>`fldsbnQLwOZz4WVnr` | `singleLineText` | Type: singleLineText |  |
| **MetaCampaignID**<br>`fldznBHqldjdOpV0z` | `singleLineText` | Type: singleLineText |  |
| **ConfigHash**<br>`fldbj1PLidPs3ChPP` | `singleLineText` | Type: singleLineText |  |
| **PreviousConfigHash**<br>`fldYtbtFf731ZaBtZ` | `singleLineText` | Type: singleLineText |  |
| **IsChangeSnapshot**<br>`fldlw2T36lr03z2Sc` | `checkbox` | True/False checkbox |  |
| **ChangeType**<br>`fldEK6o2CDTUX4qzZ` | `singleLineText` | Type: singleLineText |  |
| **ChangeSummary**<br>`fldYSw0PLxGCvfhah` | `multilineText` | Multi-line text |  |
| **TargetCountryPrimary**<br>`fldGLYsQhchRUNlmw` | `singleLineText` | Type: singleLineText |  |
| **GeoKey**<br>`fld6mzPx46T64fFU2` | `singleLineText` | Type: singleLineText |  |
| **GeoLabel**<br>`fldfhlRUD0s7N84LT` | `singleLineText` | Type: singleLineText |  |
| **AgeMin**<br>`fldBaWqBPcIEId7Kv` | `number` | Numeric field |  |
| **AgeMax**<br>`fldhP74P5WWCHeytn` | `number` | Numeric field |  |
| **SocioeconomicSegment**<br>`fldrUASI3UW3zCwXF` | `singleLineText` | Type: singleLineText |  |
| **OptimizationGoal**<br>`fldG7izL6nBKjtgH7` | `singleLineText` | Type: singleLineText |  |
| **OptimizationEventMeta**<br>`fldhtZF7YkkvaffhT` | `singleLineText` | Type: singleLineText |  |
| **BudgetSource**<br>`fldVF5rZ7n1NC30iG` | `singleLineText` | Type: singleLineText |  |
| **BudgetType**<br>`fld9iUB5PmVUXlXwR` | `singleLineText` | Type: singleLineText |  |
| **BudgetAccountCurrency**<br>`fldnK1Lm3yGAckdjS` | `number` | Numeric field |  |
| **AccountCurrencyCode**<br>`fldG8mbfEcpxgFLAB` | `singleLineText` | Type: singleLineText |  |
| **PlacementsMode**<br>`fldBI6OO8c5aVnOq2` | `singleLineText` | Type: singleLineText |  |
| **TargetingJSON**<br>`flddmV4Bjf3EIPyLZ` | `multilineText` | Multi-line text |  |
| **PromotedObjectJSON**<br>`fldPMeGXJZDJ0GmRX` | `multilineText` | Multi-line text |  |
| **FullConfigJSON**<br>`fldFlNPRV35yK5Csf` | `multilineText` | Multi-line text |  |
| **AnalysisContinuityBroken**<br>`fldlrQamEwzxC6BYd` | `checkbox` | True/False checkbox |  |
| **ContinuityBreakReason**<br>`fldoIj00fayPuBYGc` | `multilineText` | Multi-line text |  |
| **SchemaVersion**<br>`fldkGz937G7QQ6w5H` | `singleLineText` | Type: singleLineText |  |
| **AdSet**<br>`fldKx8nQOBmoMc993` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Campaign**<br>`fldeVLXr6F0s3OL6i` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 19. GI_Geographies

*Table ID: `tbluvmzK1aodBRwwP`*
*Fields: 22*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **GeoKey**<br>`fldyGTF3E3lJAceZ1` | `singleLineText` | Type: singleLineText |  |
| **DisplayName**<br>`flda94VkRl2dtH8zj` | `singleLineText` | Type: singleLineText |  |
| **CountryCode**<br>`fld2e9ODX8ZincLwC` | `singleLineText` | Type: singleLineText |  |
| **CountryName**<br>`fldWJxH0vGiPyGrf3` | `singleLineText` | Type: singleLineText |  |
| **GeoLevel**<br>`fldMVfbBb8qpu7wXZ` | `singleSelect` | Single choice dropdown | `COUNTRY`, `REGION`, `PROVINCE`, `CITY`, `COMMUNE_GROUP` *(+2 more)* |
| **ParentGeoKey**<br>`fldSWIBY5Na6r9faK` | `singleLineText` | Type: singleLineText |  |
| **ParentGeography**<br>`fld1lOMJLgZBAE9oV` | `singleLineText` | Type: singleLineText |  |
| **RegionCode**<br>`fld304fJJPJ2oqBYm` | `singleLineText` | Type: singleLineText |  |
| **RegionName**<br>`fldYvwvOjDOjO1fuJ` | `singleLineText` | Type: singleLineText |  |
| **CityNames**<br>`fldxhsLfFXGeuUAOt` | `multilineText` | Multi-line text |  |
| **CommuneNames**<br>`fld8KXYpTgQBkzmiY` | `multilineText` | Multi-line text |  |
| **MetaLocationKeysJSON**<br>`fldXTuFUlNLbi6KS4` | `multilineText` | Multi-line text |  |
| **GeoDefinitionJSON**<br>`fldhQx6ndpIOSZF8c` | `multilineText` | Multi-line text |  |
| **CurrencyCode**<br>`fld7g6BWVJfsD5FHR` | `singleLineText` | Type: singleLineText |  |
| **Timezone**<br>`fldXkR4TTgHxUpE58` | `singleLineText` | Type: singleLineText |  |
| **MarketStatus**<br>`fld2aunTcb4Ky5weI` | `singleLineText` | Type: singleLineText |  |
| **Active**<br>`fldnBPqEA7tut7tm3` | `checkbox` | True/False checkbox |  |
| **Notes**<br>`fldABVLZf5fzz3pzc` | `multilineText` | Multi-line text |  |
| **CreatedAt**<br>`fld7OJIz3zaXgVEoS` | `createdTime` | Auto-generated creation time |  |
| **UpdatedAt**<br>`fldJXvHUNwBn73vn8` | `lastModifiedTime` | Auto-generated modification time |  |
| **SchemaVersion**<br>`fld5KUBUmsuAzcksy` | `singleLineText` | Type: singleLineText |  |
| **GI_AdSets**<br>`fldRDyQwpLS6M5GTE` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 20. GI_MarketingPerformanceDaily

*Table ID: `tbli1LYXYlLtdvdeD`*
*Fields: 102*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **PerformanceDailyKey**<br>`fldQwsxtGAHGoa2BA` | `singleLineText` | Type: singleLineText |  |
| **Date**<br>`fldKMt4qev2myhTDE` | `date` | Date |  |
| **MetaCampaignID**<br>`fld73oHTUTblUoNzv` | `singleLineText` | Type: singleLineText |  |
| **CampaignNameSnapshot**<br>`fldXtVRqopeDccD5m` | `singleLineText` | Type: singleLineText |  |
| **MetaAdSetID**<br>`fldPVxSepSw4YEYG7` | `singleLineText` | Type: singleLineText |  |
| **AdSetNameSnapshot**<br>`fldPG7l7brxNrOToy` | `singleLineText` | Type: singleLineText |  |
| **MetaAdID**<br>`fldZ4uV2VTnpZpwpD` | `singleLineText` | Type: singleLineText |  |
| **AdNameSnapshot**<br>`fldgfLDOI9t3g5b44` | `singleLineText` | Type: singleLineText |  |
| **CountryCode**<br>`fldog43J6oxuTB5Yp` | `singleLineText` | Type: singleLineText |  |
| **GeoKey**<br>`fldkj5FZuE2Hwv9NF` | `singleLineText` | Type: singleLineText |  |
| **GeoLabel**<br>`fld3GbR7kGdZH6wN5` | `singleLineText` | Type: singleLineText |  |
| **SocioeconomicSegment**<br>`fldRTbKkd76jcrRHc` | `singleLineText` | Type: singleLineText |  |
| **TargetRole**<br>`fldSVIeoo2tNTHtKu` | `singleLineText` | Type: singleLineText |  |
| **FunnelStage**<br>`fldPH1mERPgUfaVCf` | `singleLineText` | Type: singleLineText |  |
| **OptimizationEventMeta**<br>`fld5fApxcEYWGFO5u` | `singleLineText` | Type: singleLineText |  |
| **OptimizationEventGIEquivalent**<br>`fldAhav2S2iMtrgXy` | `singleLineText` | Type: singleLineText |  |
| **JoinStatus**<br>`fldMXvocqBE4zWU6t` | `singleLineText` | Type: singleLineText |  |
| **JoinMethod**<br>`fldanTcyjV8GYaKX3` | `singleLineText` | Type: singleLineText |  |
| **JoinWarning**<br>`flducf4h1bWQIp8AH` | `multilineText` | Multi-line text |  |
| **MetaDataPresent**<br>`fldjHNWxL6YscIwtz` | `checkbox` | True/False checkbox |  |
| **GIDataPresent**<br>`fldco6KGkgzJvRsaY` | `checkbox` | True/False checkbox |  |
| **AudienceSnapshotPresent**<br>`fldmAl1YD1EmLTj7N` | `checkbox` | True/False checkbox |  |
| **SpendAccountCurrency**<br>`fldN6oIrKh0AXxp9z` | `number` | Numeric field |  |
| **AccountCurrencyCode**<br>`fldRV0IOHabKyPkQj` | `singleLineText` | Type: singleLineText |  |
| **Impressions**<br>`fldlIv3tn6v5SbHJ7` | `number` | Numeric field |  |
| **MetaSpectatorsDaily**<br>`fld7EbLdSaDjknfvn` | `number` | Numeric field |  |
| **FrequencyDaily**<br>`fld9XG58kgbI5PPMT` | `number` | Numeric field |  |
| **ClicksAll**<br>`fldUDTVJIVVqvYu5J` | `number` | Numeric field |  |
| **LinkClicks**<br>`fldp84FDcaZifELWD` | `number` | Numeric field |  |
| **UniqueLinkClicks**<br>`fldZ2nBMyjm1jXhIe` | `number` | Numeric field |  |
| **LandingPageViewsMeta**<br>`fld5oISHicOKUFNnM` | `number` | Numeric field |  |
| **CPMAccountCurrency**<br>`fldG2Abweyvf2S27h` | `number` | Numeric field |  |
| **CTRLinkPct**<br>`fldONXovzbxAsQn46` | `percent` | Percentage |  |
| **CPCLinkAccountCurrency**<br>`fldOMxnitRM5DFP70` | `number` | Numeric field |  |
| **CostPerLPVAccountCurrency**<br>`fldRCT4SrjCOnfFpr` | `number` | Numeric field |  |
| **AudiencePotentialLower**<br>`fld2XS4hwn7TCjIw4` | `number` | Numeric field |  |
| **AudiencePotentialUpper**<br>`fldsX4h97Efk6hIiW` | `number` | Numeric field |  |
| **AudiencePotentialMidpoint**<br>`fldDQyiiHfCpGLBFO` | `number` | Numeric field |  |
| **MetaSpectatorsWindow**<br>`fldCyL4d7xYvBlrBG` | `number` | Numeric field |  |
| **ImpressionsWindow**<br>`fldlw26BwIeCDyIcG` | `number` | Numeric field |  |
| **FrequencyWindow**<br>`fldO2dieM28AKP8Dh` | `number` | Numeric field |  |
| **AudiencePenetrationMinPct**<br>`fldsXM7TpN7TfEtpW` | `percent` | Percentage |  |
| **AudiencePenetrationMidPct**<br>`fldpQPV7NWC3Vcqbb` | `percent` | Percentage |  |
| **AudiencePenetrationMaxPct**<br>`fldYITkhUOtKjWcl2` | `percent` | Percentage |  |
| **AudienceRemainingMidpoint**<br>`fldLQTL2jdNltoU0m` | `number` | Numeric field |  |
| **SpectatorGrowthPct**<br>`fldL0a1p1MUwmGLxh` | `percent` | Percentage |  |
| **IncrementalSpendPerNewSpectator**<br>`fldJrZfiqY2BHyCJN` | `number` | Numeric field |  |
| **SaturationRisk**<br>`fldpdxNRmBrDFYXLa` | `singleLineText` | Type: singleLineText |  |
| **UniqueJourneys**<br>`fldXHza3TJpFWKNml` | `number` | Numeric field |  |
| **UniqueAnonymousUsers**<br>`fldbMzoR7jm4y996H` | `number` | Numeric field |  |
| **KoruLandingViewed**<br>`fldJl0pNE6gVmIvWS` | `number` | Numeric field |  |
| **KoruQualifiedVisit**<br>`fldnbVl7INP76hG6q` | `number` | Numeric field |  |
| **KoruShareToChildCreated**<br>`fldDvtG1rNpwRuAxV` | `number` | Numeric field |  |
| **EiaLandingViewed**<br>`fldzFabcKI3IZ9o5A` | `number` | Numeric field |  |
| **EiaQualifiedVisit**<br>`fldLZ8xJWuza9QXqy` | `number` | Numeric field |  |
| **EiaShareToChildCreated**<br>`fldvMEg14VU2PeUAw` | `number` | Numeric field |  |
| **EiaSessionStarted**<br>`fldunp3w4zETsYQ82` | `number` | Numeric field |  |
| **EiaSessionCompleted**<br>`fldCPmJRiv4eL7cSu` | `number` | Numeric field |  |
| **EiaKoruCtaClicked**<br>`fldXj5gsg3ufc0KKu` | `number` | Numeric field |  |
| **KoruSignupStarted**<br>`fldlU4nkOH4JJs65D` | `number` | Numeric field |  |
| **KoruFreemiumRegistered**<br>`fldK6PvN2MlFXTKuD` | `number` | Numeric field |  |
| **KoruActivationAchieved**<br>`fldCADjF1MQAnyy9d` | `number` | Numeric field |  |
| **PremiumStarted**<br>`fldb9q9PCZPC5Li1O` | `number` | Numeric field |  |
| **PremiumRetained30d**<br>`fldG1OG3cTFADEFpS` | `number` | Numeric field |  |
| **PremiumRetained90d**<br>`fldQgPYi3b9oOpv2Y` | `number` | Numeric field |  |
| **ReferralFreemiumRegistered**<br>`fldWgyBiGEIuEPGkp` | `number` | Numeric field |  |
| **ReferralPremiumStarted**<br>`fldQMLXJXS234HthM` | `number` | Numeric field |  |
| **GILandingPer1000Impressions**<br>`fldi6jfECJDYYPILD` | `number` | Numeric field |  |
| **GIQualifiedPer1000Impressions**<br>`fldThQMTwDAFU24dx` | `number` | Numeric field |  |
| **EiaStartsPer1000Impressions**<br>`fldTXXOqfvPQFvYVR` | `number` | Numeric field |  |
| **FreemiumPer1000Impressions**<br>`fldb2AihBwRE1v1kx` | `number` | Numeric field |  |
| **ActivationsPer1000Impressions**<br>`fldnDmTutbX22g4Sf` | `number` | Numeric field |  |
| **PremiumPer1000Impressions**<br>`fldmBvB1kHbUlsXLq` | `number` | Numeric field |  |
| **MetaLPVPerLinkClickPct**<br>`fld1d1p06tDmrj7bH` | `percent` | Percentage |  |
| **GILandingPerLinkClickPct**<br>`fldGRLZr2XaIDvgHx` | `percent` | Percentage |  |
| **EiaStartRatePct**<br>`fldVVYKtebSudQwpH` | `percent` | Percentage |  |
| **EiaCompletionRatePct**<br>`fldv8YCS07DWV2fBz` | `percent` | Percentage |  |
| **EiaToKoruRatePct**<br>`fldHrCzIofIdP4BUh` | `percent` | Percentage |  |
| **SignupCompletionRatePct**<br>`fld1CbZATgWkvRcuM` | `percent` | Percentage |  |
| **FreemiumActivationRatePct**<br>`fld9fjjwnkfW1JILT` | `percent` | Percentage |  |
| **PremiumFromFreemiumRatePct**<br>`fldXVK1TDlxDHfPtE` | `percent` | Percentage |  |
| **CostPerGIQualifiedVisit**<br>`fldiT3LRyVHgZbv1E` | `number` | Numeric field |  |
| **CostPerEiaSessionStarted**<br>`fldPZB3ge97TfLarb` | `number` | Numeric field |  |
| **CostPerEiaSessionCompleted**<br>`fldEmrdnt5b8UvKVe` | `number` | Numeric field |  |
| **CostPerShareToChild**<br>`fldIUVLL54kJGlbBU` | `number` | Numeric field |  |
| **CostPerKoruFreemium**<br>`fldMZpPXZHyIkGG0U` | `number` | Numeric field |  |
| **CostPerKoruActivation**<br>`fldS19OjiOgL6SZk2` | `number` | Numeric field |  |
| **CostPerPremiumStarted**<br>`fldMs9KJAD6TmeUhH` | `number` | Numeric field |  |
| **CostPerPremiumRetained90d**<br>`fldjStxuBbRXBQQRk` | `number` | Numeric field |  |
| **ScalabilityStatus**<br>`fldRwDP5LRymqjNSU` | `singleLineText` | Type: singleLineText |  |
| **SaturationAssessment**<br>`fld8Q8tZgk06IP3El` | `multilineText` | Multi-line text |  |
| **EfficiencyAssessment**<br>`fldJfXrU3Fj4r1t8s` | `multilineText` | Multi-line text |  |
| **DataConfidenceLevel**<br>`fldQXKOXqk1Tlxfbe` | `singleLineText` | Type: singleLineText |  |
| **RecommendedAction**<br>`fld9PbavQ4ItZYPEu` | `singleLineText` | Type: singleLineText |  |
| **RecommendationRationale**<br>`fldLD8JTjFsldhSF2` | `multilineText` | Multi-line text |  |
| **CalculatedAt**<br>`fldPqpt47qqQDbubC` | `dateTime` | Date and time |  |
| **CalculationVersion**<br>`fldvdCQkPBuWuO5Vu` | `singleLineText` | Type: singleLineText |  |
| **CalculationRunID**<br>`fld7yzK0Ch14boPiD` | `singleLineText` | Type: singleLineText |  |
| **SchemaVersion**<br>`fldrBjeuDG7oaLNVD` | `singleLineText` | Type: singleLineText |  |
| **Campaign**<br>`fldx1qhhW6gPz9IDi` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AdSet**<br>`fldns1ZvQdRytdWuo` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Ad**<br>`fld1jkeE1mWZ6EfR3` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 21. GI_MetaAdsDaily

*Table ID: `tbl02ac5cwozcVG3z`*
*Fields: 47*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **MetaDailyKey**<br>`fldupMrZmRKvPjZWH` | `singleLineText` | Type: singleLineText |  |
| **Date**<br>`fldvUrUgDbj3Hp7uT` | `date` | Date |  |
| **MetaAccountID**<br>`fldrA3VDwONNgI3pZ` | `singleLineText` | Type: singleLineText |  |
| **MetaCampaignID**<br>`flddUpltwgtnrKbnA` | `singleLineText` | Type: singleLineText |  |
| **CampaignNameSnapshot**<br>`fldjIZgUUTzneArYf` | `singleLineText` | Type: singleLineText |  |
| **MetaAdSetID**<br>`fld6okY5xt5eQOr6V` | `singleLineText` | Type: singleLineText |  |
| **AdSetNameSnapshot**<br>`fldIvnK17DazXGSUd` | `singleLineText` | Type: singleLineText |  |
| **MetaAdID**<br>`fldrtIrtxaqGQeBCH` | `singleLineText` | Type: singleLineText |  |
| **AdNameSnapshot**<br>`fldP9z2bWKCRweL9H` | `singleLineText` | Type: singleLineText |  |
| **CountryCode**<br>`fldLQX62DVAdvJ7MV` | `singleLineText` | Type: singleLineText |  |
| **GeoKey**<br>`fldiRJMBgrESWK49T` | `singleLineText` | Type: singleLineText |  |
| **SocioeconomicSegment**<br>`fldfaWMddkOEmo07t` | `singleLineText` | Type: singleLineText |  |
| **TargetRole**<br>`fldHLxz0fWgUAWmZX` | `singleLineText` | Type: singleLineText |  |
| **SpendAccountCurrency**<br>`fldV4XtYPjJKeEIfP` | `number` | Numeric field |  |
| **AccountCurrencyCode**<br>`fldHHY7a2YPDHFq6P` | `singleLineText` | Type: singleLineText |  |
| **Impressions**<br>`fldO0hsEbn7atgche` | `number` | Numeric field |  |
| **MetaSpectatorsDaily**<br>`fldlAZpbBNPwi4aT7` | `number` | Numeric field |  |
| **FrequencyDaily**<br>`fldFfMRQYRyHOr4S9` | `number` | Numeric field |  |
| **ClicksAll**<br>`fldS08rlCT1Jw55Ng` | `number` | Numeric field |  |
| **LinkClicks**<br>`flddsuRCeJrPOjGt5` | `number` | Numeric field |  |
| **UniqueLinkClicks**<br>`fldZjr24kk8gKf25Q` | `number` | Numeric field |  |
| **LandingPageViewsMeta**<br>`fldTPoUXW05XgvMH0` | `number` | Numeric field |  |
| **CPMAccountCurrency**<br>`fldBX0jjVUQQXpzEN` | `number` | Numeric field |  |
| **CTRAllPct**<br>`fldqQod70gS4DRngG` | `percent` | Percentage |  |
| **CTRLinkPct**<br>`fldQjzjwwLznktEUR` | `percent` | Percentage |  |
| **CPCAllAccountCurrency**<br>`fldS3Xyj8ZfN46jRu` | `number` | Numeric field |  |
| **CPCLinkAccountCurrency**<br>`fldZDZBHHMpb2nWzv` | `number` | Numeric field |  |
| **CostPerLPVAccountCurrency**<br>`fldObP7WNJNmEx8jg` | `number` | Numeric field |  |
| **Video3sViews**<br>`fldOZe9LHp1aAu065` | `number` | Numeric field |  |
| **Video25PctViews**<br>`fldIxEbt53HQdLeD9` | `number` | Numeric field |  |
| **Video50PctViews**<br>`fldHempz9K5u8eAP5` | `number` | Numeric field |  |
| **Video75PctViews**<br>`fldBd6imp1Dgk0Mlj` | `number` | Numeric field |  |
| **Video95PctViews**<br>`fldQyTh7yGxUMaBQa` | `number` | Numeric field |  |
| **Video100PctViews**<br>`fldyLKmiq2fJJol8t` | `number` | Numeric field |  |
| **ThruPlays**<br>`fldtjbVtcE6O4GW8A` | `number` | Numeric field |  |
| **ImportedAt**<br>`fld0XhjMTYotwA2ee` | `dateTime` | Date and time |  |
| **MetaApiVersion**<br>`fldeeoo9E7vfAXPRW` | `singleLineText` | Type: singleLineText |  |
| **ImportRunID**<br>`fldeRI1H9T9ahodam` | `singleLineText` | Type: singleLineText |  |
| **RawActionsJSON**<br>`fldv116Vv4NntV3Am` | `multilineText` | Multi-line text |  |
| **RawCostPerActionJSON**<br>`fldxKXFUfoS3ZJq7m` | `multilineText` | Multi-line text |  |
| **RawInsightJSON**<br>`fldewG6E7cOmRj8MR` | `multilineText` | Multi-line text |  |
| **ImportStatus**<br>`fldQCFPqocnajE8VL` | `singleLineText` | Type: singleLineText |  |
| **ImportError**<br>`fldKwooaqeUHwSctr` | `multilineText` | Multi-line text |  |
| **SchemaVersion**<br>`fldZu7WqY1AGVxgi7` | `singleLineText` | Type: singleLineText |  |
| **Campaign**<br>`fld1gxYRtyfviMONT` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AdSet**<br>`fldaoTV3WpGneWwGI` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Ad**<br>`fldhbZsvwrKXCg1kO` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 22. GI_MetaAudienceSnapshots

*Table ID: `tblC0GcmCE3egQTzU`*
*Fields: 36*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **AudienceSnapshotKey**<br>`fldEFCbwMNrdBdLpQ` | `singleLineText` | Type: singleLineText |  |
| **SnapshotDate**<br>`fldBEmqOVuCgpqKOk` | `date` | Date |  |
| **SnapshotAt**<br>`fldIwUXTrgnVA1BCe` | `dateTime` | Date and time |  |
| **WindowType**<br>`fldmFA0qnAoTJp1Kn` | `singleLineText` | Type: singleLineText |  |
| **WindowStartDate**<br>`fldL7Z351M3W5EfND` | `date` | Date |  |
| **WindowEndDate**<br>`fldzpHWoBmaQgE295` | `date` | Date |  |
| **MetaCampaignID**<br>`fldyBIAFqebw9sdee` | `singleLineText` | Type: singleLineText |  |
| **MetaAdSetID**<br>`fldKubDrDQtzIEUwn` | `singleLineText` | Type: singleLineText |  |
| **CountryCode**<br>`fldxOLZ0d1b4SbZC4` | `singleLineText` | Type: singleLineText |  |
| **GeoKey**<br>`fldmpnESqsmVDpPAT` | `singleLineText` | Type: singleLineText |  |
| **ConfigHash**<br>`fldBMwFcLYbRNy6Kl` | `singleLineText` | Type: singleLineText |  |
| **AudiencePotentialLower**<br>`fldaUaUgvE5y2AHrA` | `number` | Numeric field |  |
| **AudiencePotentialUpper**<br>`fldU7dJSF56q85Sbh` | `number` | Numeric field |  |
| **AudiencePotentialMidpoint**<br>`fldeUmKexhQuuFr3Q` | `number` | Numeric field |  |
| **MetaSpectatorsWindow**<br>`fldIbJwd26jqEGBd6` | `number` | Numeric field |  |
| **ImpressionsWindow**<br>`fldY2ASIlR5IaOduU` | `number` | Numeric field |  |
| **FrequencyWindow**<br>`fldm7yqI05l0utSDw` | `number` | Numeric field |  |
| **SpendWindowAccountCurrency**<br>`fldo410NpdrBK96OI` | `number` | Numeric field |  |
| **AccountCurrencyCode**<br>`fldUt34LUO0uAlPMn` | `singleLineText` | Type: singleLineText |  |
| **AudiencePenetrationMinPct**<br>`fldBlJ9TW3fecj2h4` | `percent` | Percentage |  |
| **AudiencePenetrationMidPct**<br>`fldmc9M29PTe9bYQu` | `percent` | Percentage |  |
| **AudiencePenetrationMaxPct**<br>`fldDJeCO02K08VOAI` | `percent` | Percentage |  |
| **AudienceRemainingMidpoint**<br>`fldYC1M9C0glHK6Is` | `number` | Numeric field |  |
| **NewSpectatorsVsPreviousWindow**<br>`fldpypSdM8GCjmQAF` | `number` | Numeric field |  |
| **SpectatorGrowthPct**<br>`fldwgLQfFEaxxUL5Q` | `percent` | Percentage |  |
| **IncrementalSpendPerNewSpectator**<br>`fldrXYVPMKuTMzixo` | `number` | Numeric field |  |
| **SaturationRisk**<br>`fldvX1ZS2eAXIHCPx` | `singleLineText` | Type: singleLineText |  |
| **AudienceEstimateStatus**<br>`fldpHRZltY8Nnhzq1` | `singleLineText` | Type: singleLineText |  |
| **AudienceEstimateCapturedAt**<br>`fld3tHB0RPdiisJuq` | `dateTime` | Date and time |  |
| **ImportedAt**<br>`fldPFiOTJgUWJnAEY` | `dateTime` | Date and time |  |
| **RawAudienceEstimateJSON**<br>`fldfvTfzhAsNKUO9k` | `multilineText` | Multi-line text |  |
| **RawInsightsWindowJSON**<br>`fldtmwTRVlmycqYpY` | `multilineText` | Multi-line text |  |
| **ErrorDetail**<br>`fld1CNVfOuNtf8u27` | `multilineText` | Multi-line text |  |
| **SchemaVersion**<br>`fld3npV1yzzElzwrh` | `singleLineText` | Type: singleLineText |  |
| **Campaign**<br>`fld2syuVXZklaGR0A` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **AdSet**<br>`fldBrQOPSHdGVixTQ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 23. GrowthAnalysis

*Table ID: `tblXmupIWtoGJugZh`*
*Fields: 15*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **AnalysisID**<br>`fldfDigWJh5pPdWiM` | `singleLineText` | Type: singleLineText |  |
| **AnalysisType**<br>`flde9S43DGbwp7icX` | `singleLineText` | Type: singleLineText |  |
| **PeriodStart**<br>`fldEyZIBYipYHXlrU` | `dateTime` | Date and time |  |
| **PeriodEnd**<br>`fldEdBXaD0aM0mks8` | `dateTime` | Date and time |  |
| **DataSnapshotID**<br>`fldMYJgsGqUGEAQHB` | `singleLineText` | Type: singleLineText |  |
| **ExecutiveSummary**<br>`fldVnPQOzvWXkyM47` | `multilineText` | Multi-line text |  |
| **Findings**<br>`fldxbrJyEu2aUwE2i` | `multilineText` | Multi-line text |  |
| **Anomalies**<br>`fldazKxGtXBbxMVRx` | `multilineText` | Multi-line text |  |
| **SegmentsToAct**<br>`fldLJF1M8JLvyWFIG` | `multilineText` | Multi-line text |  |
| **Hypotheses**<br>`fld0kxPKWg9n0gprd` | `multilineText` | Multi-line text |  |
| **RecommendedActions**<br>`fldmdnxOZoyOXXJrz` | `multilineText` | Multi-line text |  |
| **Priority**<br>`fld1cqJPlwUchXze1` | `singleLineText` | Type: singleLineText |  |
| **HumanDecision**<br>`fldp9Z1lUJeGI5KdT` | `multilineText` | Multi-line text |  |
| **ActionStatus**<br>`fldVO2jk0KWPFedHT` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldcR8SyBVLr8hL4Y` | `dateTime` | Date and time |  |

---

## 📋 24. InstitutionStudentValidation

*Table ID: `tbl0n5bQdK5QHLA5n`*
*Fields: 8*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ValidationID**<br>`fld5rMsy8mtXlBJZA` | `singleLineText` | Type: singleLineText |  |
| **InstitutionID**<br>`fldIPVH2K4kxE8cEN` | `singleLineText` | Type: singleLineText |  |
| **CohortID**<br>`fldjca6ON0Ov6lQAM` | `singleLineText` | Type: singleLineText |  |
| **StudentNationalIDHash**<br>`fldQx4VL6YYBSectF` | `singleLineText` | Type: singleLineText |  |
| **StudentNationalIDLast4**<br>`fldbVlEz9atoE1TDx` | `singleLineText` | Type: singleLineText |  |
| **Status**<br>`fldFbVOxFQ8ER0ewQ` | `singleLineText` | Type: singleLineText |  |
| **ValidationMethod**<br>`fldpsO5dCJ9pHpES3` | `singleLineText` | Type: singleLineText |  |
| **LastValidatedAt**<br>`fld5bNJXe4yRQF7P7` | `dateTime` | Date and time |  |

---

## 📋 25. Leads

*Table ID: `tblUq5FfmdnAp1ozz`*
*Fields: 21*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Mail**<br>`fld5cTnmu1E9J3VrJ` | `email` | Email address |  |
| **Nombre**<br>`fldNjhvgvQ7e9hfSL` | `singleLineText` | Type: singleLineText |  |
| **FechaCreacion**<br>`fldJ75dBlmGzlCXWu` | `createdTime` | Auto-generated creation time |  |
| **FechaEnvioRegalo**<br>`fld6QQ8q3rtCObL8J` | `dateTime` | Date and time |  |
| **FechaRetargeting24hrs**<br>`fldDftksolpjrdKAh` | `dateTime` | Date and time |  |
| **Pais**<br>`fldvSD5nFm9vV16vY` | `singleSelect` | Single choice dropdown | `AR`, `BO`, `BR`, `CL`, `CO` *(+5 more)* |
| **UTMSource**<br>`fldF8yOPC75xkpwKh` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fld4p4cwe0IGKSRhv` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldCZV4qsTgTuLo1b` | `singleLineText` | Type: singleLineText |  |
| **Compro**<br>`fldMdEs1PA0XtLkRg` | `checkbox` | True/False checkbox |  |
| **flagEnvioMail**<br>`fldkdso2b3HgnLPOE` | `formula` | Calculated field | Formula: `IF(
  AND(
    {fldNjhvgvQ7e9hfSL}!="",{fld5cTnm...` |
| **Whatsapp**<br>`fldZQ4qUODNbrtENq` | `phoneNumber` | Phone number |  |
| **FormatoPreferido**<br>`fldRqaDn6v6ZQiX8X` | `singleLineText` | Type: singleLineText |  |
| **PrecioAceptable**<br>`fldd85tNWYixY9UBd` | `singleLineText` | Type: singleLineText |  |
| **ProblemaMedioPago**<br>`fldAJUriXuRi76k79` | `multilineText` | Multi-line text |  |
| **InteresTaller**<br>`fldPf04EFIr8Eflf2` | `singleLineText` | Type: singleLineText |  |
| **OrigenLead**<br>`fldeqrDPLxI68Iqoq` | `singleSelect` | Single choice dropdown | `Libro`, `KORU`, `EIA`, `OF` |
| **EIA_SesionOrigen**<br>`fldckLG1rG31cvxda` | `singleLineText` | Type: singleLineText |  |
| **RolDeclarado**<br>`fldyQjqe8OeyiPn64` | `singleSelect` | Single choice dropdown | `estudiante`, `madre_padre_tutor`, `docente`, `estudios_superiores`, `otro` |
| **AceptaComunicaciones**<br>`fld35obEf3kDw0kQX` | `checkbox` | True/False checkbox |  |
| **EIA_Sesiones**<br>`fldy8wIkrmpw9Z93s` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 26. Logros

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

## 📋 27. IdentityMap

*Table ID: `tblhI6JhkpHEH6GN4`*
*Fields: 36*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **IdentityID**<br>`fldlSXfE0IBkIqAC4` | `singleLineText` | Type: singleLineText |  |
| **AnonID**<br>`fld8aRvadceuxC2Vd` | `singleLineText` | Type: singleLineText |  |
| **DeviceID**<br>`fldtVuqIqURawXFiH` | `singleLineText` | Type: singleLineText |  |
| **Email**<br>`fldNHIm4AhWgrpS6d` | `singleLineText` | Type: singleLineText |  |
| **EmailHash**<br>`fldPtVA9A9faLcwfq` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldHF7X9y2iU1noHL` | `singleLineText` | Type: singleLineText |  |
| **LeadID**<br>`fldiLpiwEZtjEbtGm` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fld6vKgrJIftkDdUj` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldnez4XleZxYachA` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fld3HLLQCfFytPEsq` | `singleLineText` | Type: singleLineText |  |
| **FirstSeenAt**<br>`fldibKtmXtREiL0ED` | `dateTime` | Date and time |  |
| **LastSeenAt**<br>`fldAiwCtLbgIjla5p` | `dateTime` | Date and time |  |
| **Confidence**<br>`fldUkW0alEvinMYhB` | `singleLineText` | Type: singleLineText |  |
| **Source**<br>`fldGk2IRKOduxeop7` | `singleLineText` | Type: singleLineText |  |
| **IdentityKey**<br>`fldTJuLBnr0iaElbP` | `singleLineText` | Type: singleLineText |  |
| **IdentificationLevel**<br>`fld3XThNK4880mysR` | `singleLineText` | Type: singleLineText |  |
| **IsIdentified**<br>`fldhedK1sfLbVfnzD` | `checkbox` | True/False checkbox |  |
| **Environment**<br>`fldSp9KchQWij2rda` | `singleLineText` | Type: singleLineText |  |
| **FirstJourneyID**<br>`fldrjRw2GoVmpJ0hV` | `singleLineText` | Type: singleLineText |  |
| **LastJourneyID**<br>`fldBjYds9vjBvxW9j` | `singleLineText` | Type: singleLineText |  |
| **RootJourneyID**<br>`fldwMF1lmkARMV6p5` | `singleLineText` | Type: singleLineText |  |
| **FirstEventID**<br>`fldEcYdvCkQkq7bQ4` | `singleLineText` | Type: singleLineText |  |
| **FirstEventName**<br>`fldRx1cO8wIXOpS9w` | `singleLineText` | Type: singleLineText |  |
| **FirstEventTime**<br>`fldoGIPj8woVzMuWp` | `dateTime` | Date and time |  |
| **FirstEventRecordID**<br>`fldkArQkh0H3xVU86` | `singleLineText` | Type: singleLineText |  |
| **LastEventID**<br>`fldE35VPhW4oXeNVR` | `singleLineText` | Type: singleLineText |  |
| **LastEventName**<br>`fldSbM3ZOnbnY9sge` | `singleLineText` | Type: singleLineText |  |
| **LastEventTime**<br>`fldrFuWuLZGF4dIGP` | `dateTime` | Date and time |  |
| **LastEventRecordID**<br>`fldXf3TXtRbVrfPKF` | `singleLineText` | Type: singleLineText |  |
| **FirstProductContext**<br>`fldZDMupd9taUXbYV` | `singleLineText` | Type: singleLineText |  |
| **LastProductContext**<br>`fld6bjg0BnI0Uk913` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldBmNDvgXyGwcJEL` | `dateTime` | Date and time |  |
| **UpdatedAt**<br>`fld9Uysm228hh9KAP` | `dateTime` | Date and time |  |
| **EventCount**<br>`fldWIiGxV2pFyydfv` | `number` | Numeric field |  |
| **LastPageURL**<br>`fldqAR5jiKyZSJHfJ` | `multilineText` | Multi-line text |  |
| **LastPropertiesJSON**<br>`fldMAjtfrPMhG3aXW` | `multilineText` | Multi-line text |  |

---

## 📋 28. Institutions

*Table ID: `tblktrYx0Sglt9KRz`*
*Fields: 12*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **InstitutionID**<br>`fld0cxn3oAUfioZRS` | `singleLineText` | Type: singleLineText |  |
| **Country**<br>`fld6Gj5wu7e8Ai2n9` | `singleLineText` | Type: singleLineText |  |
| **InstitutionOfficialID**<br>`fldWSIIhPaMeX8blV` | `singleLineText` | Type: singleLineText |  |
| **InstitutionOfficialIDType**<br>`fldaVYW7yfo2gccNF` | `singleLineText` | Type: singleLineText |  |
| **InstitutionName**<br>`fldHOfSjVRNynaKIy` | `singleLineText` | Type: singleLineText |  |
| **City**<br>`fldSZAYSJEy2ZfJ4y` | `singleLineText` | Type: singleLineText |  |
| **Commune**<br>`fldhTuR8GqrxTgoBo` | `singleLineText` | Type: singleLineText |  |
| **Region**<br>`fldxw5Ytn4DdrPSnM` | `singleLineText` | Type: singleLineText |  |
| **AgreementStatus**<br>`fldHnBhe0ry5ueB0x` | `singleLineText` | Type: singleLineText |  |
| **AgreementStartDate**<br>`fldm2ffppdGYhO9de` | `date` | Date |  |
| **AgreementEndDate**<br>`fldsk1H69mRxjsQ0r` | `date` | Date |  |
| **EIAAccessLevel**<br>`fldnyTMxChi6dP6QI` | `singleLineText` | Type: singleLineText |  |

---

## 📋 29. InstitutionCohorts

*Table ID: `tblS66znKQeq0Jm5M`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **CohortID**<br>`fldclHxAQXNXemN5Z` | `singleLineText` | Type: singleLineText |  |
| **InstitutionID**<br>`fldH66XxsRvJgisH6` | `singleLineText` | Type: singleLineText |  |
| **Country**<br>`fldnvgzPiMTwDBuf1` | `singleLineText` | Type: singleLineText |  |
| **AcademicYear**<br>`fldHxkqSPg8d4kjSq` | `singleLineText` | Type: singleLineText |  |
| **LevelCanonical**<br>`fldVvhJbRDxGyYGgS` | `number` | Numeric field |  |
| **CourseSection**<br>`fldhj9bMmus8VbQTn` | `singleLineText` | Type: singleLineText |  |
| **CourseCanonical**<br>`fldqUjdheUzSHHxNi` | `singleLineText` | Type: singleLineText |  |
| **CourseLocalLabel**<br>`fldFyMqaWd3faDPKi` | `singleLineText` | Type: singleLineText |  |
| **EIAAccessLevel**<br>`fldKfUw9JsH3w3whj` | `singleLineText` | Type: singleLineText |  |

---

## 📋 30. Interventions

*Table ID: `tblrnar4DJ2wzFEaA`*
*Fields: 20*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **InterventionID**<br>`fld8Yhzkipi3mdBBe` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldwwY1fR3vWymzvL` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldXBVzH269fxVsNL` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldKExwenVHyLBUSx` | `singleLineText` | Type: singleLineText |  |
| **InterventionType**<br>`fldS6H8Xdes7cqsdH` | `singleLineText` | Type: singleLineText |  |
| **TriggerReason**<br>`fldoKxypp4n12s0Za` | `multilineText` | Multi-line text |  |
| **TriggerEventID**<br>`fldSjiMTkXXeP3dW6` | `singleLineText` | Type: singleLineText |  |
| **LifecycleStageAtTrigger**<br>`fldsXa4SeTSL7gEhC` | `singleLineText` | Type: singleLineText |  |
| **CreditsGranted**<br>`fldAAxKC0Hl2ySllr` | `number` | Numeric field |  |
| **CreditsType**<br>`fldSFg3SbBrUH44aU` | `singleLineText` | Type: singleLineText |  |
| **MessageSent**<br>`fldMTXzU7NiDzDB5k` | `multilineText` | Multi-line text |  |
| **Channel**<br>`fldbEbi0Fwg2kHaEx` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldnAX3d1lNhHeato` | `dateTime` | Date and time |  |
| **DeliveredAt**<br>`fldqZ07B2Ue6jK1G4` | `dateTime` | Date and time |  |
| **OpenedAt**<br>`fldaQs6evaZxqZsUJ` | `dateTime` | Date and time |  |
| **ClickedAt**<br>`fldeMaTt9I6jDQGcy` | `dateTime` | Date and time |  |
| **RedeemedAt**<br>`fld7nijkwVZ636CjB` | `dateTime` | Date and time |  |
| **OutcomeWindowDays**<br>`fldfgamXNEo4Fx2cr` | `number` | Numeric field |  |
| **OutcomeEvent**<br>`fldCZWVRSheZUFt7I` | `singleLineText` | Type: singleLineText |  |
| **OutcomeSuccess**<br>`fld6WReZHGvwqNmDh` | `checkbox` | True/False checkbox |  |

---

## 📋 31. Journeys

*Table ID: `tbldtnGZk2RHFYoFI`*
*Fields: 101*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **JourneyID**<br>`fldJayXjhqjZRnOZE` | `singleLineText` | Type: singleLineText |  |
| **RootAnonID**<br>`fldUBZhhAXFOOHKmQ` | `singleLineText` | Type: singleLineText |  |
| **RootPersonID**<br>`fldX4yJ932Q7GV2Yv` | `singleLineText` | Type: singleLineText |  |
| **FirstTouchpointID**<br>`fldomzt9Dc7ytiQLQ` | `singleLineText` | Type: singleLineText |  |
| **FirstSeenAt**<br>`fldeRhsYzJdYPayrd` | `dateTime` | Date and time |  |
| **LastSeenAt**<br>`fld1N5PUFuDjmqIJg` | `dateTime` | Date and time |  |
| **CurrentStage**<br>`fldZ0fBwMqLkgzK38` | `singleLineText` | Type: singleLineText |  |
| **AcquisitionPath**<br>`fldMILBHI178XrPi4` | `multilineText` | Multi-line text |  |
| **FirstTouchChannel**<br>`flddc9c6Jayp1H9Fk` | `singleLineText` | Type: singleLineText |  |
| **FirstTouchCampaign**<br>`fldVA3racGgGtZEGJ` | `singleLineText` | Type: singleLineText |  |
| **LastTouchChannel**<br>`fld0icHXbjg7JCXH9` | `singleLineText` | Type: singleLineText |  |
| **LastTouchCampaign**<br>`fldz9IYVhL6Oaxqbl` | `singleLineText` | Type: singleLineText |  |
| **RootChainChannel**<br>`fldCbMPYqTo56jlgd` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fldcooslRSH8aZZWv` | `singleLineText` | Type: singleLineText |  |
| **ShareDepthMax**<br>`fld8SA5kgsTRyVZC2` | `number` | Numeric field |  |
| **HasMother**<br>`fld71lgXspwGUp2f3` | `checkbox` | True/False checkbox |  |
| **HasStudent**<br>`fldko1xBuM8Vh6VZR` | `checkbox` | True/False checkbox |  |
| **HasInstitution**<br>`fld8iwYJuwKleP2Ru` | `checkbox` | True/False checkbox |  |
| **HasEIA**<br>`fldaDlAstSn6mYTjq` | `checkbox` | True/False checkbox |  |
| **HasKoruFreemium**<br>`fldYnW3W4HxVzJToa` | `checkbox` | True/False checkbox |  |
| **HasKoruActivation**<br>`fldzbES50d7vrPCsm` | `checkbox` | True/False checkbox |  |
| **HasPremium**<br>`fldYLDp4E3GbfFI8i` | `checkbox` | True/False checkbox |  |
| **PremiumStartedAt**<br>`fldOnDlryfMLMaGVm` | `dateTime` | Date and time |  |
| **CurrentLTV**<br>`fld7ktDXx1K83sOO0` | `number` | Numeric field |  |
| **RootJourneyID**<br>`fldIMNOUSi5Vg3TMs` | `singleLineText` | Type: singleLineText |  |
| **LastEventName**<br>`fld2qWXWugAZJbwqT` | `singleLineText` | Type: singleLineText |  |
| **FirstEventName**<br>`fldz6AKV6rrwL2LMO` | `singleLineText` | Type: singleLineText |  |
| **FirstEventID**<br>`fldIRN58897cTo9jf` | `singleLineText` | Type: singleLineText |  |
| **FirstEventTime**<br>`fldt6hcVyFpG2v0c5` | `dateTime` | Date and time |  |
| **FirstEventRecordID**<br>`fldf01ofB83DstRXn` | `singleLineText` | Type: singleLineText |  |
| **ParentJourneyID**<br>`fld5nhikC4PS913NQ` | `singleLineText` | Type: singleLineText |  |
| **Environment**<br>`fldg0nWNTwqbes0rv` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fldBywfbHZLhotAq3` | `singleLineText` | Type: singleLineText |  |
| **Status**<br>`fldjKZjWkEwXMCsOV` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldcj2Du0islkOhMl` | `dateTime` | Date and time |  |
| **UpdatedAt**<br>`fldfncaa0k2MSYS3h` | `dateTime` | Date and time |  |
| **LastEventID**<br>`fldusoCXGBerB4xq4` | `singleLineText` | Type: singleLineText |  |
| **LastEventTime**<br>`fldFa9LPvNALoBxqX` | `dateTime` | Date and time |  |
| **LastEventRecordID**<br>`fldWEmOQnjyfQPBLD` | `singleLineText` | Type: singleLineText |  |
| **EventCount**<br>`fldMGoAdBTnju4Dnv` | `number` | Numeric field |  |
| **AnonID**<br>`fldSguJSqBuxolIaB` | `singleLineText` | Type: singleLineText |  |
| **PersonID**<br>`fldbgT52UicxRSFXQ` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldVR6XzmtDbPnou1` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldY03l52vfqqBfFd` | `singleLineText` | Type: singleLineText |  |
| **CountryDetected**<br>`fldyGGSOK2vhc6bad` | `singleLineText` | Type: singleLineText |  |
| **CountrySelected**<br>`fldha9KrK32wG9gTi` | `singleLineText` | Type: singleLineText |  |
| **CountryForAnalysis**<br>`fldgxLuyADqoVPsZl` | `singleLineText` | Type: singleLineText |  |
| **UTMSource**<br>`fldSRO5FY61gRAY7l` | `singleLineText` | Type: singleLineText |  |
| **UTMMedium**<br>`fldOdoDzdioT5EPtV` | `singleLineText` | Type: singleLineText |  |
| **UTMCampaign**<br>`fldPHdV2lCybd4vKJ` | `singleLineText` | Type: singleLineText |  |
| **UTMContent**<br>`fldDx4Nbdrbb0wpB3` | `singleLineText` | Type: singleLineText |  |
| **UTMTerm**<br>`fldkrVwlN5xdM7eqn` | `singleLineText` | Type: singleLineText |  |
| **Fbclid**<br>`fldvO7YW4c77FW9A4` | `singleLineText` | Type: singleLineText |  |
| **Gclid**<br>`fld099uNURBbkCoyg` | `singleLineText` | Type: singleLineText |  |
| **Referrer**<br>`fldK9NtQ1hhDeH9xV` | `singleLineText` | Type: singleLineText |  |
| **LandingPageURL**<br>`fldnUp9UjlV6tRY3c` | `singleLineText` | Type: singleLineText |  |
| **LastPageURL**<br>`fld5DhdKiAYcOlvpG` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldGUcHiPvfS6Yfxq` | `singleLineText` | Type: singleLineText |  |
| **ReferralID**<br>`fldvfW3iw9F2PIQKA` | `singleLineText` | Type: singleLineText |  |
| **FirstPropertiesJSON**<br>`fldxjw9BOCaTv1BQi` | `multilineText` | Multi-line text |  |
| **LastPropertiesJSON**<br>`fld3L1TV2wpg6DHFO` | `multilineText` | Multi-line text |  |
| **HasQualifiedVisit**<br>`fldytIph9kcBTPmfM` | `checkbox` | True/False checkbox |  |
| **QualifiedVisitAt**<br>`fldH6CN5RZ8kjYYjD` | `dateTime` | Date and time |  |
| **HasCTAClicked**<br>`fldPeedWcykNBfa7f` | `checkbox` | True/False checkbox |  |
| **FirstCTAClickedAt**<br>`fldj5SM2DsiVXvjtk` | `dateTime` | Date and time |  |
| **HasEIAStarted**<br>`fldhduVOJgEeiFOnj` | `checkbox` | True/False checkbox |  |
| **EIAStartedAt**<br>`fld4vCBNOIZU1mzgG` | `dateTime` | Date and time |  |
| **HasEIACompleted**<br>`fldXpEyH8EltgIPDY` | `checkbox` | True/False checkbox |  |
| **EIACompletedAt**<br>`fldkztxf09DOBuViC` | `dateTime` | Date and time |  |
| **HasSignupStarted**<br>`fldFnHPTm70KlZPo4` | `checkbox` | True/False checkbox |  |
| **SignupStartedAt**<br>`fldD5ivI2c13t84K5` | `dateTime` | Date and time |  |
| **FreemiumRegisteredAt**<br>`fldCoqjLAvgXE47Vy` | `dateTime` | Date and time |  |
| **HasFreemiumRegistered**<br>`fldpnYEkfZls52005` | `checkbox` | True/False checkbox |  |
| **HasFirstSessionStarted**<br>`fld86jVNzPp7QsGes` | `checkbox` | True/False checkbox |  |
| **FirstSessionStartedAt**<br>`fldgvTqf2v6CsZRxA` | `dateTime` | Date and time |  |
| **HasFirstSessionCompleted**<br>`fldVdtedXlzkWj8jX` | `checkbox` | True/False checkbox |  |
| **FirstSessionCompletedAt**<br>`fldvtSuTOlRFxadwt` | `dateTime` | Date and time |  |
| **HasSecondSessionCompleted**<br>`fldie6eaWCGDdVpc0` | `checkbox` | True/False checkbox |  |
| **SecondSessionCompletedAt**<br>`fldppp23zlNQ7dF9k` | `dateTime` | Date and time |  |
| **HasActivationAchieved**<br>`fldodvwNCGgm1uQhh` | `checkbox` | True/False checkbox |  |
| **ActivationAchievedAt**<br>`fldIHMFevCVQRxG08` | `dateTime` | Date and time |  |
| **HasPremiumCheckoutStarted**<br>`fldlS2mVt1NlJgwBj` | `checkbox` | True/False checkbox |  |
| **PremiumCheckoutStartedAt**<br>`fldP4101gfNdHqxth` | `dateTime` | Date and time |  |
| **HasPremiumPaymentCompleted**<br>`fld2rDATiLc5NXdCq` | `checkbox` | True/False checkbox |  |
| **PremiumPaymentCompletedAt**<br>`fldxXL9Cad2ksfEns` | `dateTime` | Date and time |  |
| **HasPremiumStarted**<br>`fldrlnbUdOpLXIdRC` | `checkbox` | True/False checkbox |  |
| **FirstTouchCapturedAt**<br>`fldn4OMowCJwmXldH` | `dateTime` | Date and time |  |
| **LastTouchCapturedAt**<br>`fldPZYfpSu0JfcgHe` | `dateTime` | Date and time |  |
| **LastUTMSource**<br>`fld8a6HkrBdYHddRC` | `singleLineText` | Type: singleLineText |  |
| **LastUTMMedium**<br>`fldYo4G8XCcb4jmex` | `singleLineText` | Type: singleLineText |  |
| **LastUTMCampaign**<br>`fldpjIjkBVJUxCo6G` | `singleLineText` | Type: singleLineText |  |
| **LastUTMContent**<br>`fldmS3pXGXCOpv4JH` | `singleLineText` | Type: singleLineText |  |
| **LastUTMTerm**<br>`fldH4iTSBK7LBqBgW` | `singleLineText` | Type: singleLineText |  |
| **LastFbclid**<br>`fldmjed2brrbODYWJ` | `singleLineText` | Type: singleLineText |  |
| **LastGclid**<br>`fldps7j39BSZ0cGg9` | `singleLineText` | Type: singleLineText |  |
| **LastReferrer**<br>`fldPqZ8JnsHNCCmY6` | `multilineText` | Multi-line text |  |
| **LastTouchEventID**<br>`fldfnR7WuB6COc02Y` | `singleLineText` | Type: singleLineText |  |
| **LastTouchEventName**<br>`fldK9qXQM9ReXLUnf` | `singleLineText` | Type: singleLineText |  |
| **DateTime**<br>`fldgj5v613zzCvoEf` | `dateTime` | Date and time |  |
| **SingleLineText**<br>`fldv3wNU1qJiBqkyV` | `singleLineText` | Type: singleLineText |  |
| **LastTouchPageURL**<br>`fldxxGXdkcOggPtWb` | `multilineText` | Multi-line text |  |

---

## 📋 32. KORU_Doors

*Table ID: `tblgRuPrxH1Pk2I5Z`*
*Fields: 8*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **DoorID**<br>`fldyuBHsmh6CwFWm4` | `singleLineText` | Type: singleLineText |  |
| **DoorKey**<br>`fldOeQ8NCLNvRpC64` | `singleLineText` | Type: singleLineText |  |
| **DoorName**<br>`fld6tNWyqMIvHSp1L` | `singleLineText` | Type: singleLineText |  |
| **DoorCategory**<br>`fldnk3D7VlBczHg0I` | `singleLineText` | Type: singleLineText |  |
| **IsFreemiumAvailable**<br>`fldiXDRBj8nr3uxkE` | `checkbox` | True/False checkbox |  |
| **IsPremiumOnly**<br>`fldWqXP61tJZQPGp8` | `checkbox` | True/False checkbox |  |
| **Status**<br>`fldWvLZFMiqoe2cKR` | `singleLineText` | Type: singleLineText |  |
| **StrategicRole**<br>`fldWjqsHrQzcEz1hz` | `multilineText` | Multi-line text |  |

---

## 📋 33. KORU_DoorUsage

*Table ID: `tblWgFOENkynO54Or`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **DoorUsageID**<br>`fldRYmsV03zZkV5N2` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldyx6qcpEfV8IvRj` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldTDJ3gqMP1pUJbm` | `singleLineText` | Type: singleLineText |  |
| **SessionID**<br>`fld7PP5l4lv76p4pf` | `singleLineText` | Type: singleLineText |  |
| **DoorKey**<br>`fldaua6Ek56Iehoa6` | `singleLineText` | Type: singleLineText |  |
| **StartedAt**<br>`flduQWdSDRUpZF19T` | `dateTime` | Date and time |  |
| **CompletedAt**<br>`fldqytOVgQJVsqueD` | `dateTime` | Date and time |  |
| **DurationSeconds**<br>`fldKABXfMuaaFznOW` | `number` | Numeric field |  |
| **MessageCount**<br>`fldXT37OCYEpwxyiV` | `number` | Numeric field |  |
| **LearningWin**<br>`fldyTwc6PkwB2KAIZ` | `checkbox` | True/False checkbox |  |
| **GapDetected**<br>`fldPlqDQVRt57hcnp` | `checkbox` | True/False checkbox |  |
| **GapWorked**<br>`fld1onFmii2LHOiFI` | `checkbox` | True/False checkbox |  |
| **UpgradeClicked**<br>`fldwza65xpOocH4ep` | `checkbox` | True/False checkbox |  |
| **PlanAtUsage**<br>`fldn1myMYziaqHjuD` | `singleLineText` | Type: singleLineText |  |

---

## 📋 34. Mensajes

*Table ID: `tblk3NUMOZhQX42AJ`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Mensaje**<br>`fldICiv65DcYl0ZMO` | `autoNumber` | Type: autoNumber |  |
| **Conversacion**<br>`fld0lhvJqLpoX8lzh` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Estudiante**<br>`fldsDJlGdYydWEjzD` | `multipleLookupValues` | Type: multipleLookupValues |  |
| **Rol**<br>`fldrBWwu17uehpmwN` | `singleSelect` | Single choice dropdown | `estudiante`, `asistente`, `sistema` |
| **Contenido**<br>`fldskyjOSEa80QeoI` | `richText` | Rich text with formatting |  |
| **TokensUsados**<br>`fld7kXyt2mxu2jff8` | `number` | Numeric field |  |
| **ModeloIA**<br>`fld0hzK2Pf0nah5Uq` | `singleLineText` | Type: singleLineText |  |
| **Timestamp**<br>`fldrycW7y7bBFaLUy` | `createdTime` | Auto-generated creation time |  |
| **ContieneImagen**<br>`fld8ohAvc4OTu8d7K` | `checkbox` | True/False checkbox |  |
| **MetricasDiarias**<br>`fldPbYZ1ceJdydjrN` | `singleLineText` | Type: singleLineText |  |
| **CostoMensaje**<br>`fldSYiKZmNSUahvGN` | `number` | Numeric field |  |
| **TokensInput**<br>`fldziuynjZAoI8SX8` | `number` | Numeric field |  |
| **TokensCacheados**<br>`fldeErlTg8gBN3FGz` | `number` | Numeric field |  |
| **TokensOutput**<br>`fldc4tqbAiLmMGCCc` | `number` | Numeric field |  |

---

## 📋 35. MetricasDiarias

*Table ID: `tblgF1aCbdkC8PWU7`*
*Fields: 17*

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
| **TokensCacheados**<br>`fld7cuB3fK8dRg9ZO` | `number` | Numeric field |  |
| **PctCacheHit**<br>`fld6wqh7gUiVX3tbd` | `number` | Numeric field |  |
| **CostoReal**<br>`fldfcE1sACpSs5NOV` | `number` | Numeric field |  |
| **CostoEstimado	**<br>`fldJjSPpuvmsEmOmP` | `currency` | Currency amount |  |
| **CostoEstimado**<br>`fldvrqhG9Zl8j4KQr` | `currency` | Currency amount |  |

---

## 📋 36. MetricasNEE

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

## 📋 37. Pagadores

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

## 📋 38. Pagos

*Table ID: `tbllGZKmZYWmRTZk1`*
*Fields: 19*

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
| **RecID**<br>`fld91PuEdA6qy3WNF` | `formula` | Calculated field | Formula: `RECORD_ID()` |
| **CreatedTime**<br>`fldiJdoGtCHWUZjcx` | `createdTime` | Auto-generated creation time |  |

---

## 📋 39. ParametrosGenerales

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

## 📋 40. PlanesEstudio

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

## 📋 41. PostulacionesConvenios

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

## 📋 42. PremiumRetention

*Table ID: `tblgXY6cEvMdzA9cK`*
*Fields: 33*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **PremiumRetentionID**<br>`fldBTgClQSJB7YcpF` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldEZoQgigtFtkXcd` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`fldLEScsvivyVOl5j` | `singleLineText` | Type: singleLineText |  |
| **PagadorID**<br>`fldu4q7OupQT66Qmd` | `singleLineText` | Type: singleLineText |  |
| **PremiumStartDate**<br>`fld3g4nQvQ9e2o8gB` | `dateTime` | Date and time |  |
| **CurrentPremiumStatus**<br>`fld2G2edorbK3xc27` | `singleLineText` | Type: singleLineText |  |
| **CurrentRetentionStage**<br>`fldFgQXm3zrJFhoeO` | `singleLineText` | Type: singleLineText |  |
| **PremiumStartedBeforeActivation**<br>`fldiyeUOX2CHqGkFp` | `checkbox` | True/False checkbox |  |
| **PremiumActivationAfterPaymentDays**<br>`fldzNLX1roLGbKxUV` | `number` | Numeric field |  |
| **DaysAsPremium**<br>`fldmR0Xx8RbxKW0iE` | `number` | Numeric field |  |
| **PaymentsSucceeded**<br>`fld6y1PsQX1vKdYfF` | `number` | Numeric field |  |
| **PaymentsFailed**<br>`fldwkliNQnjsWcHry` | `number` | Numeric field |  |
| **RenewalsSucceeded**<br>`fldbgBLQkw61QtXRW` | `number` | Numeric field |  |
| **RenewalsFailed**<br>`fldzAqyyhV5LhNRyf` | `number` | Numeric field |  |
| **LastPaymentDate**<br>`fldIXjrhvGOmHaSM4` | `dateTime` | Date and time |  |
| **NextPaymentDate**<br>`fldXdDkI4oOoNU1vi` | `dateTime` | Date and time |  |
| **ChurnDate**<br>`fld9kWKx4rkoYVG1u` | `dateTime` | Date and time |  |
| **PremiumDaysToChurn**<br>`fldgiMh4y5ykD4N9U` | `number` | Numeric field |  |
| **PremiumSessionsTotal**<br>`fldz0oSMfuWFSWIDl` | `number` | Numeric field |  |
| **PremiumActiveDaysTotal**<br>`fldaPNZfVAESajFM7` | `number` | Numeric field |  |
| **PremiumSessionsPerWeekLifetime**<br>`fldWzVtsb8Z70AExB` | `number` | Numeric field |  |
| **PremiumSessionsPerWeekLast30d**<br>`flds67ZsIDnd7zJMc` | `number` | Numeric field |  |
| **PremiumSessionsPerWeekLast60d**<br>`fldOOyvbK2I9d5LH2` | `number` | Numeric field |  |
| **PremiumLast30dSessions**<br>`fld0yLBFCrEPHE7mN` | `number` | Numeric field |  |
| **PremiumLast60dSessions**<br>`fldr5vQIMrtKOe8Xr` | `number` | Numeric field |  |
| **PremiumLast90dSessions**<br>`fldAmlatAXE5TVQSi` | `number` | Numeric field |  |
| **PremiumLearningWinsTotal**<br>`fldvW67I3ZWuJFJWm` | `number` | Numeric field |  |
| **PremiumLearningWinsLast30d**<br>`fldXjcBTqtE379YfG` | `number` | Numeric field |  |
| **PremiumDoorsUsedTotal**<br>`fld2lGjrI8NBmWJJb` | `number` | Numeric field |  |
| **PremiumMotherTouchpointsTotal**<br>`fldw1Wg7nGu35CVOA` | `number` | Numeric field |  |
| **ChurnRiskScore**<br>`fldWQ9u095feqr5aS` | `number` | Numeric field |  |
| **LTVAccrued**<br>`fldavOrN0AvhjwY7E` | `number` | Numeric field |  |
| **ExpectedLTV**<br>`fldMd2m8noQpC3L1A` | `number` | Numeric field |  |

---

## 📋 43. Recordatorios

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

## 📋 44. RecursosDidacticos

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

## 📋 45. ReferralEdges

*Table ID: `tbl8sMgQGao1wFsri`*
*Fields: 15*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ReferralEdgeID**<br>`fld5imjU9a9JvVPPS` | `singleLineText` | Type: singleLineText |  |
| **FromPersonID**<br>`fldtGKdpsUCRtj0Ch` | `singleLineText` | Type: singleLineText |  |
| **FromAnonID**<br>`fldH9x0L4Lz9xjQVm` | `singleLineText` | Type: singleLineText |  |
| **ToPersonID**<br>`fldi7qrqkGQwGaqFs` | `singleLineText` | Type: singleLineText |  |
| **ToAnonID**<br>`fldj5CGXuNMGRa4a8` | `singleLineText` | Type: singleLineText |  |
| **ShareLinkID**<br>`fldNPhWpBvzMvfPs1` | `singleLineText` | Type: singleLineText |  |
| **ParentShareLinkID**<br>`fldNqDbsk1fuU4Arc` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fldyTkOFkdNxzYQO5` | `singleLineText` | Type: singleLineText |  |
| **Depth**<br>`fldMJVtYZSAxRZ6BZ` | `number` | Numeric field |  |
| **RelationshipDeclared**<br>`fldOdr36CSQvDpjD3` | `singleLineText` | Type: singleLineText |  |
| **Confidence**<br>`fldv5i3PSMltTIPlA` | `singleLineText` | Type: singleLineText |  |
| **FirstSeenAt**<br>`flduIwv1XtqpoMiEl` | `dateTime` | Date and time |  |
| **ConvertedToLead**<br>`fldm7D3uk5U4o9ILL` | `checkbox` | True/False checkbox |  |
| **ConvertedToFreemium**<br>`fldPjEPm7dvfHgRYD` | `checkbox` | True/False checkbox |  |
| **ConvertedToPremium**<br>`fldGx8mRUz1IJKfsF` | `checkbox` | True/False checkbox |  |

---

## 📋 46. Segments

*Table ID: `tbldNS4mwf2RzggKH`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **SegmentID**<br>`fldtoWOb4jKErDYto` | `singleLineText` | Type: singleLineText |  |
| **SegmentKey**<br>`fldIL4anmPNgnoa54` | `singleLineText` | Type: singleLineText |  |
| **SegmentName**<br>`fldZkj97PJJ6jAi84` | `singleLineText` | Type: singleLineText |  |
| **Description**<br>`fldEdRyVaDh1fc2Jb` | `multilineText` | Multi-line text |  |
| **CriteriaJSON**<br>`fldQXfseyg5l1TPhI` | `multilineText` | Multi-line text |  |
| **LastCalculatedAt**<br>`fldhlrITioyUcmVhC` | `dateTime` | Date and time |  |
| **UsersCount**<br>`flddw3iWaZvlR24Ur` | `number` | Numeric field |  |
| **RecommendedAction**<br>`fldpuF9nPW9MOtozK` | `multilineText` | Multi-line text |  |
| **Destination**<br>`fldcoonpRvl1XVm7P` | `singleLineText` | Type: singleLineText |  |

---

## 📋 47. Seguimiento

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

## 📋 48. SenalesDeInteres

*Table ID: `tblPykEYkqBz98oXJ`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Senal**<br>`fldVpPXXWsimQ5coL` | `autoNumber` | Type: autoNumber |  |
| **Detalle**<br>`fld7PSYXqd5KQ9bHe` | `singleLineText` | Type: singleLineText |  |
| **PlanAlMomento**<br>`fldtf858JccLSphnO` | `singleLineText` | Type: singleLineText |  |
| **ModalidadPremium**<br>`fld8DjmAOOzM7KGEJ` | `singleLineText` | Type: singleLineText |  |
| **Procesada**<br>`fld2l9fgDWRG7B7g6` | `checkbox` | True/False checkbox |  |
| **FechaProcesada**<br>`fldfRAt8MG7rigWG1` | `dateTime` | Date and time |  |
| **Estudiante**<br>`fldWWHDb6didV3TpF` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FechaSenal**<br>`fldhDwE7CO6Zys7IC` | `createdTime` | Auto-generated creation time |  |
| **TipoSenal**<br>`fld1HHTyfvKFZxqlN` | `singleLineText` | Type: singleLineText |  |

---

## 📋 49. SesionesEstudio

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

## 📋 50. ShareLinks

*Table ID: `tbl3r2cxqEYYgKlcW`*
*Fields: 21*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ShareLinkID**<br>`fldrQw2y0Bj6fXu3i` | `singleLineText` | Type: singleLineText |  |
| **ShareCode**<br>`fldUpDVjijtS4Uoge` | `singleLineText` | Type: singleLineText |  |
| **ProductContext**<br>`fld2RIlbmfnVbI9H8` | `singleLineText` | Type: singleLineText |  |
| **CreatedByPersonID**<br>`fldKiBw9Z5e3yWsvf` | `singleLineText` | Type: singleLineText |  |
| **CreatedByAnonID**<br>`fldKAbLmcOU0b3BGf` | `singleLineText` | Type: singleLineText |  |
| **CreatedByRole**<br>`fldbxHRg2p4SK09Tj` | `singleLineText` | Type: singleLineText |  |
| **CreatedFromEventID**<br>`fld35b2BDbTABtsIS` | `singleLineText` | Type: singleLineText |  |
| **RootTouchpointID**<br>`fldV8mBLUANQdPmMu` | `singleLineText` | Type: singleLineText |  |
| **RootCampaignID**<br>`fldTC5IvJWB0e9WEy` | `singleLineText` | Type: singleLineText |  |
| **ParentShareLinkID**<br>`fld4CvaLMs1Y075UM` | `singleLineText` | Type: singleLineText |  |
| **RootShareLinkID**<br>`fld5MN2OTxp8V872O` | `singleLineText` | Type: singleLineText |  |
| **ShareDepth**<br>`fldN2WUVtdNGD6K5U` | `number` | Numeric field |  |
| **ShareChannel**<br>`fldSn3CTzqRuRwRnD` | `singleLineText` | Type: singleLineText |  |
| **ShareIntent**<br>`fldgQgSMk8OzrWpry` | `singleLineText` | Type: singleLineText |  |
| **CreatedAt**<br>`fldrRka4yvPUNBL0n` | `dateTime` | Date and time |  |
| **Clicks**<br>`fldV7EYiHtLzDV4oY` | `number` | Numeric field |  |
| **UniqueClicks**<br>`fldbLrJOqec5xNJRG` | `number` | Numeric field |  |
| **ConversionsToLead**<br>`fldmBOpPz5nkEYQsK` | `number` | Numeric field |  |
| **ConversionsToEIA**<br>`fld3jZKEMztqL82RU` | `number` | Numeric field |  |
| **ConversionsToFreemium**<br>`fldzEMqCvIFZb2ukl` | `number` | Numeric field |  |
| **ConversionsToPremium**<br>`fldHQ85EZYAdzX1Qj` | `number` | Numeric field |  |

---

## 📋 51. Suscripciones

*Table ID: `tblowJOhwqRvVsWWc`*
*Fields: 37*

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
| **OrigenPlan**<br>`fldngwoOT5egJSN7z` | `singleSelect` | Single choice dropdown | `Paddle`, `Beca`, `Promo` |
| **CodigoBeca**<br>`fldosUk4QMbNpNeHJ` | `singleLineText` | Type: singleLineText |  |
| **Estudiantes 2 copy**<br>`fldKXGhRQ14TK6jfG` | `singleLineText` | Type: singleLineText |  |
| **recID**<br>`fldw90Kt5IVYi473M` | `formula` | Calculated field | Formula: `RECORD_ID()` |
| **ModifiedTime**<br>`fldo7vfZA52Pbtw7T` | `lastModifiedTime` | Auto-generated modification time |  |

---

## 📋 52. Testimonios

*Table ID: `tblLkbXyveEP7z1mj`*
*Fields: 22*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **ID_Testimonio**<br>`fldHD2YIvCXLTeVAW` | `autoNumber` | Type: autoNumber |  |
| **Estudiante**<br>`fldyGNwU6ehdzphjU` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **NombreMostrar**<br>`fldiYRcHa5IXLbzYN` | `singleLineText` | Type: singleLineText |  |
| **Edad**<br>`fldb9XLkUR3WOQC2b` | `number` | Numeric field |  |
| **Texto**<br>`fldW6WG2g4srYx6Wi` | `multilineText` | Multi-line text |  |
| **ImagenURL**<br>`fld793C7UxXgOPybX` | `url` | URL link |  |
| **Pais**<br>`fldUOJwGkb3HXaHSb` | `singleSelect` | Single choice dropdown | `Argentina`, `Bolivia`, `Chile`, `Colombia`, `Ecuador` *(+7 more)* |
| **TiposNEE**<br>`fldUH5HL7DjBDWMd4` | `multipleSelects` | Multiple choice dropdown | `Discalculia`, `Dislexia`, `Ninguno`, `TDA`, `TDAH` *(+1 more)* |
| **ConversacionesAlEnviar**<br>`fldwiH6KtS8fXyMFS` | `number` | Numeric field |  |
| **FechaEnvio**<br>`fldrri5YW5bZXzTm9` | `createdTime` | Auto-generated creation time |  |
| **Estado**<br>`fldXHOUtCWekNqt2Z` | `singleSelect` | Single choice dropdown | `Aprobado`, `Pendiente`, `Postergado`, `Rechazado` |
| **FechaRevision**<br>`fldtns8ORRpSmd2Bt` | `dateTime` | Date and time |  |
| **NotasInternas**<br>`fldz7MP6ncg871Hc2` | `multilineText` | Multi-line text |  |
| **MostrarEnLanding**<br>`fldjw1jYZXPYXjsEc` | `checkbox` | True/False checkbox |  |
| **MostrarAvisos**<br>`fldbdIfRI4DUUCWSn` | `checkbox` | True/False checkbox |  |
| **Consentimiento**<br>`fld2hlrv4i57szQQa` | `checkbox` | True/False checkbox |  |
| **FechaConsentimiento**<br>`fldrllRRz6Tem6tsx` | `dateTime` | Date and time |  |
| **Pregunta1**<br>`fld3zJioBO6LNgC6W` | `singleSelect` | Single choice dropdown | `Sí`, `No` |
| **Pregunta2**<br>`fldi8KdJc9CBpe6Sg` | `singleSelect` | Single choice dropdown | `Me ha servido mucho`, `Me ha servido algo`, `Me ha servido poco`, `No me ha servido` |
| **Pregunta3**<br>`fld0Gm1fj5k7WSQ9M` | `singleSelect` | Single choice dropdown | `Mucho`, `Bastante`, `Algo`, `Nada` |
| **Pregunta4**<br>`fldzOr0UCuGgNP5cU` | `singleSelect` | Single choice dropdown | `Aprender algo puntual`, `Preparar una evaluación`, `Aprender a estudiar` |
| **Pregunta5**<br>`fld4KRIEkdHvac59M` | `singleSelect` | Single choice dropdown | `Mucho, me asombra`, `Bastante`, `Lo percibo débilmente`, `No lo he notado` |

---

## 📋 53. UserLifecycleWindows

*Table ID: `tblpM9Y8euDQZ3tMq`*
*Fields: 36*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **WindowID**<br>`fldQJrCpDSflC7qYH` | `singleLineText` | Type: singleLineText |  |
| **StudentID**<br>`fldxFIJWItbBWskFS` | `singleLineText` | Type: singleLineText |  |
| **FamilyID**<br>`flddS3i5p1gOoaFC9` | `singleLineText` | Type: singleLineText |  |
| **WindowType**<br>`fldNXWWgjgRtOTOJS` | `singleLineText` | Type: singleLineText |  |
| **WindowNumber**<br>`fldOIkaDnJVwdEGmA` | `number` | Numeric field |  |
| **WindowStart**<br>`fldiHh4JZcGXo1aHY` | `dateTime` | Date and time |  |
| **WindowEnd**<br>`fldfYTds4NlFP9sWM` | `dateTime` | Date and time |  |
| **DaysFromSignupStart**<br>`fldPIunZOKdWBs1VZ` | `number` | Numeric field |  |
| **DaysFromPremiumStart**<br>`fldzc2WEuePFjlPpM` | `number` | Numeric field |  |
| **SessionsCount**<br>`fldEtQV3hjqDrQbke` | `number` | Numeric field |  |
| **CompletedSessionsCount**<br>`fldie14ROpTxR8CEa` | `number` | Numeric field |  |
| **ActiveDaysCount**<br>`fldlP1WGxxKvMqPaD` | `number` | Numeric field |  |
| **AvgSessionsPerWeek**<br>`fldlfZ8jaCZZMqVYv` | `number` | Numeric field |  |
| **AvgSessionDuration**<br>`fldoEDJ96CxFz5bLM` | `number` | Numeric field |  |
| **TotalMessages**<br>`fld6zl2u2MFdvKQBQ` | `number` | Numeric field |  |
| **LearningWinsCount**<br>`fldKCWvZ4A3LmHafQ` | `number` | Numeric field |  |
| **BrechasDetectedCount**<br>`fldya3rjXBEo6N765` | `number` | Numeric field |  |
| **BrechasWorkedCount**<br>`fldfeefc42xjq96qN` | `number` | Numeric field |  |
| **DoorsUsedCount**<br>`fldWTmzmmwujN7Y5T` | `number` | Numeric field |  |
| **DoorsUsedList**<br>`flduWyH2EIJbqtsiA` | `multilineText` | Multi-line text |  |
| **FirstDoorUsed**<br>`fldIIVpMquNQsooor` | `singleLineText` | Type: singleLineText |  |
| **MostUsedDoor**<br>`flds6FfFBpztDUi3B` | `singleLineText` | Type: singleLineText |  |
| **DoorSequence**<br>`fldbfp4oHiuNVFKrl` | `multilineText` | Multi-line text |  |
| **LockedDoorClicks**<br>`fldMw6viRgKySdXtb` | `number` | Numeric field |  |
| **EIAUsedCount**<br>`fldOkPI4ysb2Sl2tL` | `number` | Numeric field |  |
| **EIAScoreDeltaAvg**<br>`fldy2f95iSh0oyKSe` | `number` | Numeric field |  |
| **SharesTotalTimes**<br>`fldVpkPNB5XpltWMs` | `number` | Numeric field |  |
| **SharesEiaTimes**<br>`flduChIzblddClHVZ` | `number` | Numeric field |  |
| **SharesKoruTimes**<br>`fld8LxcOtkFnPKb1m` | `number` | Numeric field |  |
| **ShareClicksGenerated**<br>`fldL5rbt2HBn4cJXX` | `number` | Numeric field |  |
| **ReferralLeadsGenerated**<br>`flduPkkJbZbm7SVVH` | `number` | Numeric field |  |
| **ReferralFreemiumsGenerated**<br>`fldiPVAbRQktqwILf` | `number` | Numeric field |  |
| **MotherTouchpointsCount**<br>`fldNhnuad5o83H8E7` | `number` | Numeric field |  |
| **PremiumStatusAtWindowEnd**<br>`fldBrtIRdCRXusOXJ` | `singleLineText` | Type: singleLineText |  |
| **ConvertedDuringWindow**<br>`fldFfcKVMTQ2yS4zJ` | `checkbox` | True/False checkbox |  |
| **ChurnedDuringWindow**<br>`fldmaiwRFTZv4X4e4` | `checkbox` | True/False checkbox |  |

---

## 🔄 About This Documentation

### 📋 Source Information
- **Base**: Production (`prod`)
- **Base ID**: `appr2x4VzE0OySqOu`
- **Generated**: 2026-07-13 13:40:59

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
**Last sync**: 2026-07-13 13:40:59

---
*Documentation for Production base - Generated 2026-07-13 13:40:59*