# OpenSPP Proxy Means Testing

```{note}
The `spp_pmt` module has been absorbed into **`spp_scoring`** and **`spp_studio`** in OpenSPP2. This page is retained for reference and redirects to the current modules.
```

PMT (Proxy Means Test) functionality is fully available in OpenSPP2 through two modules:

- **`spp_scoring`** — handles all PMT scoring logic: indicators, weights, thresholds, calculation methods (weighted sum, CEL formula, lookup tables), and batch scoring. See {doc}`/config_guide/scoring/pmt` for configuration.
- **`spp_studio`** — includes a dedicated `pmt_targeting.xml` configuration pack that provides a ready-made PMT targeting setup through the Studio no-code interface.

## What moved where

| Old `spp_pmt` feature | Now in |
|---|---|
| PMT score calculation logic | `spp_scoring` |
| Weighted criteria configuration | `spp_scoring` (indicators + weights) |
| Area-specific weight variations | `spp_scoring` (geographic scoring support) |
| PMT score display on group form | `spp_scoring` |
| PMT targeting setup | `spp_studio` (pmt_targeting.xml pack) |

## Getting started

Install `spp_scoring` for the PMT engine. If you want a pre-built PMT targeting configuration, apply the PMT targeting pack from **Studio → Configuration Packs**.

See {doc}`/config_guide/scoring/index` for full scoring and PMT documentation.
