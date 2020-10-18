import React, { useState } from 'react'
import { format } from 'date-fns'
import { enGB } from 'date-fns/locale'
import { DatePickerCalendar, useDateInput } from '../../src'
import Example from './Example'

const code = `
`

export default function DatePickerCalendarWithInputExample() {
  const [date, setDate] = useState()

  const inputProps = useDateInput({
    date,
    format: 'yyyy-MM-dd',
    locale: enGB,
    onDateChange: setDate
  })

  return (
    <Example code={code}>
      <p>The selected date is {date && format(date, 'dd MMM yyyy', { locale: enGB })}</p>
      <input className='input' {...inputProps} />
      <DatePickerCalendar date={date} onDateChange={setDate} locale={enGB} />
    </Example>
  )
}
