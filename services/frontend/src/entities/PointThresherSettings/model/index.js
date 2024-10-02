
export class PointThresherSettings {

  constructor(HSVRanges, options) {
    this._HSVRanges = HSVRanges
    this._options = options
  }
  get HSVRanges() {
    return this._HSVRanges
  }

  get options() {
    let options = this._options
    Object.keys(this._options).forEach(key => options[key] = parseInt(options[key]))
    return options
  }

  setSettings(settings) {
    this._HSVRanges = structuredClone(settings.HSVRanges)
    this._options = structuredClone(settings.options)
  }

}



