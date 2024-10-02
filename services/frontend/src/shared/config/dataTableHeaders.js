

export const dataTableHeaders = {
  'angle': ["α, °", "t, с"],
  'amplitude': ["A, °", "τ, c"],
  'amplitude_frequency': ["A, °", "ω, рад/с"],
  'amplitude_phase_shift': ["ψ, рад", "ω, рад/с"],
}


export const getTableHeaderByDataType = (dataType) => dataTableHeaders[dataType]
