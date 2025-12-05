# 🗂️ Airtable Database Structure

> **Last update**: 2025-12-05 08:28:21
> **Auto-generated** - Do not edit manually

## 📊 Summary

- **Tables**: 15
- **Fields**: 258
- **Base ID**: `app9c8iiAYRGxxhtH`

---

## 🗃️ Brechas

*ID: `tblAHnHa5fHOPLATq`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Brecha**<br>`fldfVgj3QTW6zfzkM` | `autoNumber` |  |
| **Estudiante**<br>`fldYeKZLOTrmZx9jz` | `multipleRecordLinks` |  |
| **Materia**<br>`fldy3Letyi5rUox6u` | `singleSelect` | `Matemáticas`, `Lenguaje`, `Ciencias` (+6 more) |
| **EjeTematico**<br>`flds8wKLPjZrn7gpb` | `singleSelect` | `Álgebra`, `Números`, `Geometría` (+5 more) |
| **Contenido**<br>`fldHxwk5khjbwcS7J` | `singleLineText` |  |
| **NivelOrigen**<br>`flduhyOCgeqbK1dIw` | `singleSelect` | `5°B`, `6°B`, `7°B` (+4 more) |
| **Prioridad**<br>`fldfd60pZlnFkeZSS` | `singleSelect` | `🔴 Crítica`, `🟡 Media`, `🟢 Baja` |
| **Cerrada**<br>`fldVei33OZ1RDBj1x` | `checkbox` |  |
| **CerradaEn**<br>`flde2ELbO9RRLneRu` | `dateTime` |  |
| **DetectadaEn**<br>`fldh1cCu1VJ9P00ZK` | `createdTime` |  |

---

## 🗃️ Conversaciones

*ID: `tblhw3b9VCVrJtDu1`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Conversacion**<br>`fldhpzpygAWASqIcm` | `autoNumber` |  |
| **Estudiante**<br>`fldsFM6LQCnmLIpev` | `multipleRecordLinks` |  |
| **FechaAltaEstudiante**<br>`fldzwhZAcGxX19VAw` | `multipleLookupValues` |  |
| **TipoPuerta**<br>`fldfGrwAFFXcL5jos` | `singleSelect` | `aprender`, `preparar_evaluacion`, `mejorar_asignatura` (+2 more) |
| **Titulo**<br>`fldNkHyWabgfGAThi` | `singleLineText` |  |
| **MateriaPrincipal**<br>`fld6eG16Hs7av0euL` | `singleLineText` |  |
| **TipoNEE**<br>`fldx65y33zQeiXOsi` | `singleLineText` |  |
| **CantidadMensajes**<br>`fldQFSerbNJRUagkv` | `count` |  |
| **CantidadMensajesFinal**<br>`fldNlONZcXOGV6s2M` | `number` |  |
| **Tokens**<br>`fldtCm0VWw3wvkt0V` | `rollup` |  |
| **TokensFinal**<br>`fldaYGwxvLqtSFKws` | `number` |  |
| **CostoAPI**<br>`fldvidJST7G3PhaTs` | `formula` |  |
| **Resumen**<br>`fldLJbxM83Q7BLBfZ` | `multilineText` |  |
| **Activa**<br>`fldCvt5WUCe8du9JG` | `checkbox` |  |
| **FechaInicio**<br>`fldUuqJjygGEcscrS` | `createdTime` |  |
| **DiaSemanaInicio**<br>`fldbpEisAN1d2n4nm` | `formula` |  |
| **UltimoMensaje**<br>`fldwOV5yGkT0tiMj3` | `lastModifiedTime` |  |
| **Duracion**<br>`fld8K7xwvCEwgb64O` | `formula` |  |
| **Sugerencia**<br>`fldHO4zYmEjQ6L4Rs` | `multilineText` |  |
| **EjemploExitoso**<br>`fldYU2aABG6bgqCTt` | `checkbox` |  |
| **Calificacion**<br>`fld16ThOYVoUuiAFF` | `number` |  |
| **Mensajes**<br>`fldL6s7K9zybmNuda` | `multipleRecordLinks` |  |
| **MetricasDiarias**<br>`fldyzZZIXRSOHfm8p` | `multipleRecordLinks` |  |
| **MetricasDiarias 2**<br>`fldxn7vaqpgCVhpbO` | `singleLineText` |  |

---

## 🗃️ Mensajes

*ID: `tblk3NUMOZhQX42AJ`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Mensaje**<br>`fldICiv65DcYl0ZMO` | `autoNumber` |  |
| **Conversacion**<br>`fld0lhvJqLpoX8lzh` | `multipleRecordLinks` |  |
| **Rol**<br>`fldrBWwu17uehpmwN` | `singleSelect` | `estudiante`, `asistente`, `sistema` |
| **Contenido**<br>`fldskyjOSEa80QeoI` | `richText` |  |
| **TokensUsados**<br>`fld7kXyt2mxu2jff8` | `number` |  |
| **ModeloIA**<br>`fld0hzK2Pf0nah5Uq` | `singleSelect` | `gpt-4o`, `gpt-4o-mini`, `gpt-4-vision` |
| **Timestamp**<br>`fldrycW7y7bBFaLUy` | `createdTime` |  |
| **ContieneImagen**<br>`fld8ohAvc4OTu8d7K` | `checkbox` |  |
| **MetricasDiarias**<br>`fldPbYZ1ceJdydjrN` | `singleLineText` |  |
| **CostoMensaje**<br>`fldSYiKZmNSUahvGN` | `formula` |  |

---

## 🗃️ Curriculum

*ID: `tbld18R3UfqhagW4u`*

| Field | Type | Options |
|-------|------|---------|
| **OA**<br>`fldrjQyvXRk6shh5j` | `multilineText` |  |
| **OAserial**<br>`fld9wnfptnEeNincH` | `number` |  |
| **OAmateria**<br>`fldPPTulbJihy1UmV` | `singleSelect` | `Matemática`, `Comprensión lectora`, `Historia y Geografía` (+1 more) |
| **OAeje**<br>`fldye5FSdw7sM0DGm` | `singleSelect` | `Medición`, `Números y operaciones`, `Geometría` (+18 more) |
| **OAdescripcion**<br>`fldt3pmph8IBhENoV` | `multilineText` |  |
| **OAresumen**<br>`fld6bWr1pv2f0y27d` | `multilineText` |  |
| **OApertinenciaContenidosM1**<br>`fld9TgFlbQzFMUPyd` | `singleSelect` | `Alta`, `Media`, `Ausente` |
| **OApertinenciaHabilidadesM1**<br>`fldZMuh6JeacTUpSt` | `singleSelect` | `Alta`, `Ausente`, `Media` |
| **OAtipo**<br>`fldJjHpwQVcGduK5s` | `singleSelect` | `Basal`, `Prioritario`, `Priorización` |
| **OApertinenciaContenidosM1Respaldo**<br>`fldiPVNTu2WVLWPuR` | `multilineText` |  |
| **OAhabilidades**<br>`fldRtf2rvabm7MvhR` | `singleSelect` | `3.1. Habilidad: Resolver Problemas | 3.2. Habilidad: Modelar | 3.3. Habilidad: Representar`, `Ninguna`, `3.1. Habilidad: Resolver Problemas | 3.3. Habilidad: Representar` (+15 more) |
| **OApertinenciaHabilidadesM1Respaldo**<br>`fldgk4odkACec8b56` | `multilineText` |  |
| **OAnivel**<br>`fld2iZPfBxmNgBXA8` | `number` |  |
| **OAnivelTxt**<br>`fldqX7bbGHJFCSJb9` | `singleSelect` | `5° Básico`, `6° Básico`, `7° Básico` (+1 more) |
| **OAantiguedad**<br>`fldgT3bnJbcwkUnBD` | `number` |  |

---

## 🗃️ EjemplosPedagogicos

*ID: `tblzOij9Mx124aVEy`*

| Field | Type | Options |
|-------|------|---------|
| **ID**<br>`fld7nNpEk18RrIJ79` | `autoNumber` |  |
| **FechaCreacion**<br>`fldkAXm3fz2N3GaQO` | `date` |  |
| **TipoNEE**<br>`flddME05ykLgFBqe6` | `singleSelect` |  |
| **Materia**<br>`fld9N4GssjTlpM6Pq` | `singleSelect` | `Todo`, `In progress`, `Done` |
| **TemaEspecifico**<br>`fldT3xksy4ZxJqEMQ` | `singleLineText` |  |
| **CasoEstudio**<br>`fld9upI59cIpKYtM4` | `singleLineText` |  |
| **PromptUtilizado**<br>`fld8i2Cspjx7N8m3e` | `multilineText` |  |
| **InteraccionEstudiante**<br>`fldpMrypMehg5i8Sh` | `multilineText` |  |
| **RespuestaAsistente**<br>`fldBA0VCTRRxL02Ld` | `multilineText` |  |
| **Resultado**<br>`fldYS38LT3pnbbC7x` | `singleSelect` | `éxito`, `mejorable`, `fallo` |
| **Aprendizaje**<br>`flddqjxmk7pntxYyx` | `multilineText` |  |
| **TuRating**<br>`fld0aNINPo9rJ1cul` | `number` |  |
| **Tags**<br>`fldp9aZ3JJjHYL0mC` | `multipleSelects` | `timer`, `refuerzo_positivo`, `instrucciones_cortas` |

---

## 🗃️ Estudiantes

*ID: `tblR5gbkydy59GOOC`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Estudiante**<br>`fldp7qIUatWYG2zw2` | `autoNumber` |  |
| **Email**<br>`fldaPohMI9tlgDW4t` | `email` |  |
| **Contrasena**<br>`fld2VACy7rMKduyLP` | `multilineText` |  |
| **Rol**<br>`fld62uCAFaxkz5scC` | `singleSelect` | `Estudiante`, `Apoderado`, `Admin` |
| **Nombre**<br>`fldDs68JQokh38DX6` | `singleLineText` |  |
| **LlegoPor**<br>`fld51E4NaVZvq9upz` | `singleSelect` | `ChatGPT u otra IA`, `Convenio con tu colegio`, `Dato o consejo de un(a) amigo(a)` (+7 more) |
| **QuienDecidio**<br>`fldocqWgnEkChM2nQ` | `singleSelect` | `Yo`, `Mi padre-madre o tutor(a)` |
| **Estado**<br>`fldN9UGcBbKrtGPYD` | `singleSelect` | `Activo`, `Bloqueado`, `suspendido` |
| **Pais**<br>`fldlqQYUn3GMAVXHW` | `formula` |  |
| **PaisElegido**<br>`fld4e4pFqnpODVbJB` | `singleSelect` | `Chile`, `Argentina`, `Perú` (+9 more) |
| **CodigoPais**<br>`fldl1SW9SPvQcxIpY` | `formula` |  |
| **Celular**<br>`fldDJTv1TC3Dwr8b1` | `phoneNumber` |  |
| **NombrePreferido**<br>`fldLdC48e8cV7Qn1f` | `singleLineText` |  |
| **Curso**<br>`fldhlrRfO42asiEru` | `singleSelect` | `7 Básico`, `8 Básico`, `1 Medio` (+3 more) |
| **Edad**<br>`fldBHYunaLfzhfzNN` | `singleSelect` | `13`, `14`, `15` (+5 more) |
| **TipoEstablecimiento**<br>`fldUmNM1OokmgjnE7` | `singleSelect` | `Público (Municipal/SLEP)`, `Particular Subvencionado`, `Particular Pagado` |
| **EstiloAprendizaje**<br>`fld0ckIVlh46CtbVb` | `singleSelect` | `Visual`, `Auditivo`, `Kinestésico` (+2 more) |
| **MateriasFuertes**<br>`fldNhz8Feiohchzi1` | `singleSelect` | `Matemáticas`, `Lenguaje`, `Ciencias` (+1 more) |
| **MateriasDebiles**<br>`fldH2m6C9msfoYLRn` | `singleSelect` | `Lenguaje`, `Historia`, `Matemáticas` (+1 more) |
| **HaRepetido**<br>`fldZgc8D6koiQgda4` | `checkbox` |  |
| **TiposNEE**<br>`fld4uN4bHlLVEz3Mx` | `multipleSelects` | `TDAH`, `Dislexia`, `TEA` (+2 more) |
| **RecibePIE**<br>`fldn3Sioto5nfisur` | `checkbox` |  |
| **NivelAnsiedad**<br>`fld5u3seaJi0JePIG` | `number` |  |
| **InteresesPersonales**<br>`fldykiNRSZPdeVHw6` | `multipleSelects` | `Practicar deportes`, `Videojuegos en consola`, `Escuchar música en móvil` (+6 more) |
| **Idolo**<br>`fldlI8eMEZJCzBo7Y` | `singleLineText` |  |
| **AspiracionFutura**<br>`fldlS5kKiRrjMMLuo` | `multilineText` |  |
| **OnboardingCompletado**<br>`fld1peJxyAKgqLRg6` | `checkbox` |  |
| **FechaRegistro**<br>`fldvMB0YXrUFGNThv` | `dateTime` |  |
| **UltimaActividad**<br>`fld00gaBZOkktKJYO` | `dateTime` |  |
| **DiasDesdeUltima**<br>`fldYd2NI4ued8FXc7` | `formula` |  |
| **CantidadConversaciones**<br>`fldkF1lllYaBcR4Bl` | `formula` |  |
| **CantidadConversacionesExitosas**<br>`fldY1vwqXfZLzzn2W` | `count` |  |
| **Lunes**<br>`fldJZJ0PotO13gABR` | `count` |  |
| **Martes**<br>`fldA3hx5Y8HUCQQxe` | `count` |  |
| **Miercoles**<br>`fldT3F5dUstvcWDaK` | `count` |  |
| **Jueves**<br>`fld4HMaw3xuTrYZU5` | `count` |  |
| **Viernes**<br>`fldmNChD1n8TMgyn6` | `count` |  |
| **Sabado**<br>`fldYKlDDHfaK3G3ef` | `count` |  |
| **Domingo**<br>`fldaEGcdWiDRYl7Nc` | `count` |  |
| **Suscripciones**<br>`fldUJgVD2lFOWBZg4` | `multipleRecordLinks` |  |
| **Pagador**<br>`fldknWUUzzBo3RZ4h` | `multipleLookupValues` |  |
| **EmailPagador**<br>`fldA4uOWRPNo3IR0f` | `multipleLookupValues` |  |
| **EstadoCuentaPagador**<br>`fldZbyD2Nc89fK4MN` | `multipleLookupValues` |  |
| **FechaPago**<br>`fldUL833KTrU6As0a` | `multipleLookupValues` |  |
| **FechaProximoVencimiento**<br>`fldv97mLTiSL3s5yj` | `multipleLookupValues` |  |
| **Conversaciones**<br>`fldkSWz9udhZOD1pZ` | `multipleRecordLinks` |  |
| **Brechas**<br>`fldGzudn4tRsgmydF` | `multipleRecordLinks` |  |
| **Planes**<br>`fldKW0KGyhpogBEM9` | `singleLineText` |  |
| **Logros**<br>`fldjGdoFj8YyOa6BK` | `multipleRecordLinks` |  |
| **Recordatorios**<br>`fldUT4s4hWISFhvN0` | `multipleRecordLinks` |  |
| **EventosSignificativos**<br>`fldwNGfi1Trbu6gXi` | `multipleRecordLinks` |  |
| **recordId**<br>`fldzO8FoTnfACQMpG` | `formula` |  |
| **MetricasDiarias**<br>`fldVuv0xoETAWTGIZ` | `singleLineText` |  |
| **Pagos**<br>`fldX2wJ29vjy4LcNL` | `singleLineText` |  |
| **Suscripciones 2**<br>`fldCu7SFplfevjAgA` | `multipleRecordLinks` |  |
| **Pagadores**<br>`fldH7DEBRiJeWrWQO` | `multipleRecordLinks` |  |
| **Pagos 2**<br>`fldJnzfYBW5XHQxU8` | `multipleRecordLinks` |  |
| **TokenReset**<br>`fldObhyfttEMNyDuu` | `multilineText` |  |
| **ExpiraReset**<br>`fldM7GFnh4adVSyx2` | `dateTime` |  |

---

## 🗃️ Pagadores

*ID: `tblkl6i81e7fyKRKI`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Pagador**<br>`fldg8kZfm23qJl5xy` | `autoNumber` |  |
| **EmailPagador**<br>`fld1Q9CSkUF77j9LP` | `email` |  |
| **NombrePagador**<br>`fldkL3EyqzWW1wL4M` | `singleLineText` |  |
| **Pais**<br>`fldQbrxB2cSmt5f9R` | `singleSelect` | `Chile`, `Argentina`, `Colombia` (+1 more) |
| **Telefono**<br>`fldQhK77UwmvslBrZ` | `phoneNumber` |  |
| **MetodoPagoPreferido**<br>`fldokDvkhzblTnMdP` | `singleSelect` | `Paddle`, `MercadoPago` |
| **PaddleCustomerId**<br>`fld5pSHg2tbdnLIqU` | `singleLineText` |  |
| **EstadoCuentaPagador**<br>`fld8np85ERgOfAavC` | `singleSelect` | `Freemium`, `Premium`, `Suspendido` |
| **UltimoPago**<br>`fldsX9Bz2og25BoJE` | `date` |  |
| **ProximoPago**<br>`fldciVzK93W0RtcPQ` | `date` |  |
| **Estudiantes**<br>`fldupV0UVJjyyGduY` | `singleLineText` |  |
| **EstudiantesLink**<br>`fldmjLB3KCHZvp7HF` | `multipleRecordLinks` |  |
| **Suscripciones 2**<br>`fld22Uw0FjNQpnp6T` | `singleLineText` |  |
| **Suscripciones 2 copy**<br>`fldKZHlloJfYuHr6C` | `singleLineText` |  |
| **Pagos 2**<br>`fld8aiJlfvcRFqjx7` | `multipleRecordLinks` |  |
| **Estudiantes 2**<br>`fldVeygK325XpCUGs` | `singleLineText` |  |
| **Suscripciones**<br>`fld7g9e3zB5R9TalE` | `multipleRecordLinks` |  |
| **Suscripciones copy**<br>`fldzOJM80DzvoN1hy` | `singleLineText` |  |

---

## 🗃️ Suscripciones

*ID: `tblowJOhwqRvVsWWc`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Suscripcion**<br>`fldn1n7fwUweCvo2i` | `autoNumber` |  |
| **Estudiante**<br>`fldKyk6xVFuknhSHU` | `singleLineText` |  |
| **EstudianteLink**<br>`fldRWKk87vRLaRL2M` | `multipleRecordLinks` |  |
| **Pagador**<br>`fldC8JSN5ogRs8ISq` | `multipleRecordLinks` |  |
| **EmailPagador**<br>`fldpcfbuRcQaRsFlK` | `multipleLookupValues` |  |
| **EstadoCuentaPagador**<br>`fldQqlZbunlfXfEsG` | `multipleLookupValues` |  |
| **IDExternoPago**<br>`fldCbmS4gZ3LKmmqe` | `singleLineText` |  |
| **Pago**<br>`fldILVnRROWcJJ9LU` | `multipleRecordLinks` |  |
| **FechaPago**<br>`fldo8n5y0wZxhJ52M` | `multipleLookupValues` |  |
| **FechaProximoVencimiento**<br>`fldb1PSZ3mVGx4KS9` | `formula` |  |
| **Plan**<br>`fldaSqBvRS4GDaVI6` | `singleSelect` | `Freemium`, `Premium`, `Premium Anual` |
| **Estado**<br>`fldi8RIHJ0G746lAr` | `singleSelect` | `activa`, `cancelada`, `vencida` (+1 more) |
| **FechaInicio**<br>`fldZSINYGUXmHqqJr` | `dateTime` |  |
| **ConsultasUsadasSemana**<br>`fldwEhWwL1n2YCYmw` | `number` |  |
| **SemanaActual**<br>`fld59woiPrcvzibVY` | `date` |  |
| **UltimoPago**<br>`fld3VQmUmMaUscPLg` | `dateTime` |  |
| **MontoMensual**<br>`fldrYs1EXsSfvDAQY` | `currency` |  |
| **FechaCreacion**<br>`fldyLjf5pN8FOZtkB` | `createdTime` |  |
| **ProveedorPago**<br>`fld1kKM9eZ60X714E` | `singleSelect` | `Paddle`, `MercadoPago` |
| **AfiliadoId**<br>`fldGeGII7htfSGMbC` | `singleLineText` |  |
| **AfiliadoTipo**<br>`fld4yK0RNPkF9cGcB` | `singleSelect` | `influencer`, `docente_ambassador`, `padre_embajador` |
| **ComisionPlan**<br>`fldSn2JJhZZkjUdUl` | `singleSelect` | `recurrente_10`, `recurrente_20`, `primera_compra_30` (+1 more) |
| **UTM_Source**<br>`fldbXzXvd8qLRpq6P` | `singleLineText` |  |
| **UTM_Medium**<br>`fld7lXUePtLAFFBfk` | `singleLineText` |  |
| **UTM_Campaign**<br>`fldLFoNMyI4WeCswy` | `singleLineText` |  |
| **UltimoFalloPago**<br>`fldEHJVGJ48VA7Hrl` | `date` |  |
| **IntentosReintento**<br>`fldlSDNBOmhy2yxMH` | `number` |  |
| **SuspendidaDesde**<br>`fldOOpOl9U4WLTFfH` | `date` |  |
| **Pagos 2**<br>`fldCkH8WXaZ8OMUz9` | `multipleRecordLinks` |  |
| **Estudiantes**<br>`fldktDnYfToPEUlHK` | `multipleRecordLinks` |  |
| **Estudiantes copy**<br>`fldwYz1HMUFxlSUuB` | `singleLineText` |  |
| **Estudiantes 2**<br>`fldJQKk5HR7e9C8mV` | `singleLineText` |  |
| **Estudiantes 2 copy**<br>`fldngwoOT5egJSN7z` | `singleLineText` |  |

---

## 🗃️ Pagos

*ID: `tbllGZKmZYWmRTZk1`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Pago**<br>`fldtamvOsSzchyolz` | `singleLineText` |  |
| **Suscripcion**<br>`fldzQgXVKQJKfEAdg` | `singleLineText` |  |
| **SuscripcionLink**<br>`fldteh6mV1X0mOcJR` | `multipleRecordLinks` |  |
| **Estudiante (from SuscripcionLink)**<br>`fldFaoQYcPlHERRe9` | `multipleLookupValues` |  |
| **Pagador (from SuscripcionLink)**<br>`fldsXeO0t23vTh2n7` | `multipleLookupValues` |  |
| **Pagador**<br>`fldBLCDiPmIcG2yOF` | `singleLineText` |  |
| **PagadorLink**<br>`fldre47MsdNJIm0VX` | `multipleRecordLinks` |  |
| **EmailPagador**<br>`fldCUm6EX5urKIZF1` | `multipleLookupValues` |  |
| **Estudiante**<br>`fldk2QtZa6qC3nqan` | `singleLineText` |  |
| **EstudianteLink**<br>`fldHkWqqbUKm2LZSB` | `multipleRecordLinks` |  |
| **EstadoPago**<br>`fldXORkBWE7Czx24V` | `singleSelect` | `Exitoso`, `Fallido`, `Reembolsado` |
| **FechaPago**<br>`fldFLBDQ3aU8rUCFG` | `date` |  |
| **Monto**<br>`fldxTsBDMUAOlNLeI` | `number` |  |
| **Moneda**<br>`fldGcDvLW4rImhuMU` | `singleLineText` |  |
| **OrigenWebhook**<br>`fld1tGdy1Qrt9XHlG` | `singleLineText` |  |
| **RawPayload**<br>`fldfgKOo7FbphW8FE` | `multilineText` |  |
| **Suscripciones**<br>`fldj6NcyLD82RUqEU` | `multipleRecordLinks` |  |

---

## 🗃️ Logros

*ID: `tblIezwTdqN8x1T8H`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Logro**<br>`fldAwA7SnR5HTm03i` | `autoNumber` |  |
| **Estudiante**<br>`fldBzozokHjNTta8A` | `multipleRecordLinks` |  |
| **TipoLogro**<br>`fldhM2BYZ0XfIkM6H` | `singleSelect` | `🎯 Brecha`, `✅ Plan`, `💡 Técnica` (+1 more) |
| **Descripcion**<br>`fldLBM5BR5yMMb1gS` | `multilineText` |  |
| **Celebrado**<br>`fldmEG2JSPOy24TP9` | `checkbox` |  |
| **FechaLogro**<br>`fldeISuhbfRFcF7O1` | `createdTime` |  |

---

## 🗃️ MetricasDiarias

*ID: `tblgF1aCbdkC8PWU7`*

| Field | Type | Options |
|-------|------|---------|
| **ID**<br>`fldHDPrDh8gb6fR7h` | `autoNumber` |  |
| **Fecha**<br>`fldYyiouH6h96oy1W` | `date` |  |
| **UsuariosActivos**<br>`fld5Zj8l5ASpHH6o4` | `number` |  |
| **UsuariosNuevos**<br>`fldUaM9EiUzsZcwYc` | `number` |  |
| **ConversacionesDeHoy**<br>`fldC2o4is6XRs2b6s` | `multipleRecordLinks` |  |
| **SesionesTotales**<br>`fldX5SL4C2Gvstv7g` | `number` |  |
| **MensajesProcesados**<br>`fldeIoHc6Mml15O5G` | `number` |  |
| **ImagenesProcesadas**<br>`fld26wuwmv5ZMVzcL` | `number` |  |
| **TiempoSesionPromedio**<br>`fldjD3VhufVlCgx94` | `number` |  |
| **MateriaPrincipal**<br>`fldqJSZzHM6qSXs6v` | `singleLineText` |  |
| **EjemplosExitosos**<br>`fldP735LNZKJO3vD0` | `number` |  |
| **Errores**<br>`fldoI5Qex28nI3Tq5` | `number` |  |
| **CostoEstimado	**<br>`fldJjSPpuvmsEmOmP` | `currency` |  |

---

## 🗃️ MetricasNEE

*ID: `tblZ8HxhJrrePHPNE`*

| Field | Type | Options |
|-------|------|---------|
| **ID**<br>`fldq6vOiPmnNN7K0O` | `autoNumber` |  |
| **Fecha**<br>`fldH1YL9fkoLNgrUt` | `date` |  |
| **TipoNEE**<br>`fldGv8zGpyrkVjgsw` | `singleLineText` |  |
| **UsuariosActivos**<br>`fldOsZv0DOZ1ozZhB` | `number` |  |
| **SesionesTotales**<br>`fldGyy8JagN79lo0N` | `number` |  |
| **TasaResolucion**<br>`fldTqsR29L5vj9mjp` | `percent` |  |
| **TiempoSesionPromedio**<br>`fld26JiW2t2Xj8q2B` | `number` |  |
| **UsoImagenesPorcentaje**<br>`fldrXqInkbPBIxf8G` | `percent` |  |
| **TasaAbandono**<br>`fldNCeRR4Wmj0Dd3G` | `percent` |  |
| **SatisfaccionEstimada**<br>`fldF8Nzm8gmYd66LQ` | `number` |  |

---

## 🗃️ EventosSignificativos

*ID: `tblKU5sD9MdcTQmSH`*

| Field | Type | Options |
|-------|------|---------|
| **ID**<br>`fldlMD8qLO1qMbn3j` | `autoNumber` |  |
| **Timestamp**<br>`fldGK0v40C91xCkQD` | `dateTime` |  |
| **Usuario**<br>`fld2OiSMOXDN3dUGT` | `multipleRecordLinks` |  |
| **TipoEvento**<br>`fldH058ArfLzCuoEy` | `singleSelect` | `primera_sesion`, `resolucion_exitosa`, `sesion_larga_5min` (+4 more) |
| **Materia**<br>`fldZf4OThGc5JU7y5` | `singleLineText` |  |
| **TipoNEE**<br>`fldI6weNWvtgebLy6` | `singleLineText` |  |
| **TiempoHastaEvento**<br>`fldDjBVVgPRp2KaMO` | `number` |  |
| **DatosContexto**<br>`fld7wFo3pRTystgMN` | `multilineText` |  |

---

## 🗃️ Recordatorios

*ID: `tbll95VSiGdzEPEsZ`*

| Field | Type | Options |
|-------|------|---------|
| **ID_Recordatorio**<br>`fldCeJs9p3YhILtkp` | `autoNumber` |  |
| **Estudiante**<br>`flds4OsLlxdLog8Vl` | `multipleRecordLinks` |  |
| **Tipo**<br>`fld7GBBxkFKT87KRP` | `singleSelect` | `Plan`, `Coaching`, `Revisar` |
| **Mensaje**<br>`fldegBwIzQ4jge8hl` | `multilineText` |  |
| **FechaHora**<br>`fldNmVKZlf4pLpTfH` | `dateTime` |  |
| **Enviado**<br>`fldm1HxklxmQ8BWKR` | `checkbox` |  |
| **FechaCreacion**<br>`fldqaefpAMBXwIHYU` | `createdTime` |  |

---

## 🗃️ VERSION_PROD

*ID: `tblStqh1QgUM2ZZGE`*

| Field | Type | Options |
|-------|------|---------|
| **FechaPublicacion**<br>`fld4Vu39O4zNgLJqZ` | `dateTime` |  |
| **Ambiente**<br>`fldj1wNtXh76HZvZR` | `singleSelect` | `PROD`, `DEV` |
| **Descripción nueva versión**<br>`fldp4TVI2mIZYXWc4` | `multilineText` |  |
| **Cambios BD**<br>`fldBSosvZGrV1Gt5J` | `singleLineText` |  |
| **Descripción DB**<br>`fldLEbXdOc6yk9TI3` | `multipleAttachments` |  |
| **Cambios Automatizaciones**<br>`fldNcmh2Qu8qVpwuh` | `singleLineText` |  |
| **Archivos**<br>`fldWTvrKvV4UnvXZq` | `multipleAttachments` |  |
| **landing.html**<br>`fldczEKFzscMX6JpS` | `multilineText` |  |
| **index.html**<br>`fld7ECFpJRGQj4zJ8` | `multilineText` |  |
| **chat.js**<br>`fldSdYMAXYd2d7Bob` | `multilineText` |  |
| **config.js**<br>`fldrzHp2TJKe1Mrwn` | `multilineText` |  |
| **Prompt-chat**<br>`fld1JoX5ky69KH0st` | `multilineText` |  |
| **Worker**<br>`fldztpSTpYD3DvSlO` | `multilineText` |  |
| **WorkerDeployment**<br>`fldYNzqOOvd62mNv8` | `singleLineText` |  |
| **Version_Fillout_Onboarding**<br>`fldm1rmf4KOECMsfG` | `singleLineText` |  |

---

## 🔄 About

This document is auto-generated by GitHub Actions.
Updates daily at 8:00 AM UTC.

*Generated: 2025-12-05 08:28:21*