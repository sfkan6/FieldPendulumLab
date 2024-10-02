import { parse, derivative, re } from "mathjs";



export const getError = (func, vars, var_errors) => {
  let error = 0
  for (let arg in vars) {
    error += (re(derivative(func, arg).evaluate(vars)) * var_errors[arg])**2
  }
  return Math.sqrt(error)
}


export const getFrequencyError = (A, a, w0, b, errors) => {
  const func = parse('sqrt(-2 * b^2 + w0^2 + sqrt(4 * b^2 * (b^2 - w0^2) - (a / A)^2))')
  const vars = {'A': A, 'a': a, 'b': b, 'w0': w0}
  const varErrors = {'A': errors[0], 'a': errors[1], 'b': errors[2], 'w0': errors[3]}
  return getError(func, vars, varErrors)
}


export const getQualityFactorError = (leftFrequency, rightFrequency, resonantFrequency, errors) => {
  const func = parse('resonantFrequency / (rightFrequency - leftFrequency)')
  const vars = {'leftFrequency': leftFrequency, 'rightFrequency': rightFrequency, 'resonantFrequency': resonantFrequency}
  const varErrors = {'leftFrequency': errors[0], 'rightFrequency': errors[1], 'resonantFrequency': errors[2]}
  return getError(func, vars, varErrors)
}
