# 🗂️ Airtable Database Structure - Analytics

> **Last update**: 2026-04-10 18:16:48
> **Base**: analytics (Analytics)
> **Auto-generated** - Do not edit manually

## 📊 Summary

- **Tables**: 5
- **Total fields**: 59
- **Base ID**: `appTkMzRijzZQpL3I`

- **singleSelect fields**: 10
- **number fields**: 7
- **date fields**: 2
- **formula fields**: 7

---

## 📋 1. Cuentas

*Table ID: `tblyPykhFZSITQ5KE`*
*Fields: 9*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Nombre**<br>`fldb20kBFvtjNmF9P` | `singleLineText` | Type: singleLineText |  |
| **Tipo**<br>`fldWcj9pfCbtqMwDr` | `singleSelect` | Single choice dropdown | `Paddle`, `Meta` |
| **Entidad**<br>`fldny1JtmBkb8jGAe` | `singleSelect` | Single choice dropdown | `Raúl G. Arancibia`, `KORU SpA`, `AULAS` |
| **Producto**<br>`fldODP7K4t4bKYMJ5` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **CuentaID**<br>`fldgvtCV1kTsnUNth` | `singleLineText` | Type: singleLineText |  |
| **Ambiente**<br>`fldoSTYhijloxvPNJ` | `singleSelect` | Single choice dropdown | `Live`, `Sandbox` |
| **Activo**<br>`fldwj9NykNEH98ZSY` | `checkbox` | True/False checkbox |  |
| **VentasYPagos**<br>`fldvsBmKY67f6dYz5` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **MetricasMeta**<br>`fldn7thgds6wJwDMZ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 2. FunnelSemanal

*Table ID: `tbl9G63HWjqBR0odL`*
*Fields: 13*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **SemanaISO**<br>`fldQgMZ0T9U4J9tjt` | `singleLineText` | Type: singleLineText |  |
| **Producto**<br>`fldoxS8z8qFtyRyqx` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pais**<br>`fldkEV7ACFWrFCyun` | `singleSelect` | Single choice dropdown | `AR`, `BO`, `CL`, `CO`, `CR` *(+15 more)* |
| **GastoMeta**<br>`flduFVE6QfFcsPPs5` | `currency` | Currency amount |  |
| **VentasProducto**<br>`fld0Og2HVctdFhqrU` | `number` | Numeric field |  |
| **IngresosProducto**<br>`fldAh1bCLyidlYjEB` | `currency` | Currency amount |  |
| **RegistrosKORU**<br>`fldnAjlTVaQf2lOmx` | `number` | Numeric field |  |
| **UsuariosFreemium**<br>`fld3KQsGwUkbYjIF4` | `number` | Numeric field |  |
| **ConversionesPremium**<br>`fldllAwlFbHQmkEYF` | `number` | Numeric field |  |
| **MRR**<br>`fld1AhpvlihYjQIoo` | `currency` | Currency amount |  |
| **CostoXVenta**<br>`fldOYajdjODOWpkyA` | `formula` | Calculated field | Formula: `IF(
  {fld0Og2HVctdFhqrU}>0,{flduFVE6QfFcsPPs5}/{...` |
| **CostoXConversion**<br>`fldUNkOY5ujS5wjWZ` | `formula` | Calculated field | Formula: `IF(
  {fldllAwlFbHQmkEYF}>0,{flduFVE6QfFcsPPs5}/{...` |
| **ROI**<br>`fldqYtPflwadS6bf7` | `formula` | Calculated field | Formula: `IF(
  {flduFVE6QfFcsPPs5}>0,{fldAh1bCLyidlYjEB}/{...` |

---

## 📋 3. MetricasMeta

*Table ID: `tblpDyNQ3ILmsNsqB`*
*Fields: 13*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Fecha**<br>`fldoWa4SVeRpWk5fJ` | `date` | Date |  |
| **Cuenta**<br>`fld0QdPZ6n9A6DV2f` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Producto**<br>`fldP9QV4iRNRZ9zf3` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pais**<br>`fldOkPr2iNkSFax04` | `singleSelect` | Single choice dropdown | `AR`, `BO`, `CL`, `CO`, `CR` *(+15 more)* |
| **CampañaID**<br>`fldxVFV1Lsxfz4Rn5` | `singleLineText` | Type: singleLineText |  |
| **CampañaNombre**<br>`fldpYQWTgyiS3x8ig` | `singleLineText` | Type: singleLineText |  |
| **Gasto**<br>`fldDuDHBBrxQflCUw` | `currency` | Currency amount |  |
| **Impresiones**<br>`fldPTXmr84xM4wL2X` | `number` | Numeric field |  |
| **Clics**<br>`fldGtSRGWa9ys4wZm` | `number` | Numeric field |  |
| **Alcance**<br>`fldxm3OXxLQz9UspM` | `number` | Numeric field |  |
| **CPM**<br>`fldilSzHYPNYa41Mf` | `formula` | Calculated field | Formula: `IF({fldPTXmr84xM4wL2X}>0,{fldDuDHBBrxQflCUw}/{fldP...` |
| **CPC**<br>`fldFpc04TcslHCPEk` | `formula` | Calculated field | Formula: `IF(
  {fldGtSRGWa9ys4wZm}>0,{fldDuDHBBrxQflCUw}/{...` |
| **CTR**<br>`fldTXirSeU65SPDAV` | `formula` | Calculated field | Formula: `IF(
  {fldPTXmr84xM4wL2X}>0,{fldGtSRGWa9ys4wZm}/{...` |

---

## 📋 4. Productos

*Table ID: `tblKm2mWyoDFYtGfl`*
*Fields: 10*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **Nombre**<br>`fldxLZfxN86RhSkI2` | `singleLineText` | Type: singleLineText |  |
| **Tipo**<br>`fldKqp9Jx5U3p8U8W` | `singleSelect` | Single choice dropdown | `Libro`, `App` |
| **Entidad**<br>`fldzIda5QpVFDeXMR` | `singleSelect` | Single choice dropdown | `Raúl G. Arancibia`, `KORU SpA`, `AULAS` |
| **Activo**<br>`fldc27pJrJADYSwTF` | `checkbox` | True/False checkbox |  |
| **FechaLanzamiento**<br>`fldl5O9y72I6FwDbv` | `date` | Date |  |
| **Descripcion**<br>`flddPvCCQEoUeQmQ9` | `multilineText` | Multi-line text |  |
| **VentasYPagos**<br>`fldigxml3R3FGqC1q` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **MetricasMeta**<br>`fldd42T9YFthHU8wK` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **FunnelSemanal**<br>`fldw17eSiAPflAU05` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Cuentas**<br>`fldt6QnFT5heFoSHZ` | `multipleRecordLinks` | Type: multipleRecordLinks |  |

---

## 📋 5. VentasYPagos

*Table ID: `tbl4aZYpPHkFLOekh`*
*Fields: 14*

| Field | Type | Description | Options |
|-------|------|-------------|---------|
| **IDTransaccion**<br>`fld4doxGn1uVUBbvS` | `singleLineText` | Type: singleLineText |  |
| **Producto**<br>`fldNuNklIQdv4xBJ9` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Cuenta**<br>`fldVxEH5nQgOrzC1z` | `multipleRecordLinks` | Type: multipleRecordLinks |  |
| **Pais**<br>`fld9jlvtWthQyea0B` | `singleSelect` | Single choice dropdown | `AR`, `BO`, `CL`, `CO`, `CR` *(+15 more)* |
| **Email**<br>`fldU2VCZNYwZlSsdO` | `email` | Email address |  |
| **Nombre**<br>`fldXoAz7M119YitFS` | `singleLineText` | Type: singleLineText |  |
| **Monto**<br>`fldPeNhNWM9vdjf5V` | `currency` | Currency amount |  |
| **Moneda**<br>`fldoFDSM7iB7QpTw7` | `singleSelect` | Single choice dropdown | `USD`, `BOB`, `CLP` |
| **MontoLocal**<br>`fldQ5lJgrjUfQ7xZT` | `currency` | Currency amount |  |
| **TipoEvento**<br>`fld9Fa7ORqhQonNcD` | `singleSelect` | Single choice dropdown | `payment.succeeded`, `subscription.created`, `subscription.cancelled`, `transaction.completed` |
| **Fecha**<br>`fldTio7ESLLVtEcdr` | `dateTime` | Date and time |  |
| **DiaSemana**<br>`fldHTHHIWptq4RKiE` | `formula` | Calculated field | Formula: `SWITCH(
  WEEKDAY(SET_TIMEZONE({fldTio7ESLLVtEcdr...` |
| **FuenteUtm**<br>`fldKxH24LHDCnHUJX` | `singleLineText` | Type: singleLineText |  |
| **AtribuidoFunnel**<br>`fld8eMv2UAJ13SeCN` | `checkbox` | True/False checkbox |  |

---

## 🔄 About This Documentation

### 📋 Source Information
- **Base**: Analytics (`analytics`)
- **Base ID**: `appTkMzRijzZQpL3I`
- **Generated**: 2026-04-10 18:16:48

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
**Last sync**: 2026-04-10 18:16:48

---
*Documentation for Analytics base - Generated 2026-04-10 18:16:48*