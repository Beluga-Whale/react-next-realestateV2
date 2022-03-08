import React from 'react'
import Image from 'next/image'

const Contact = () => {
    return (
        <div className='flex bg-slate-400'>
            <div className="left"></div>
            <div className="right">
                <Image src={'/.svg'} width={704} height={657} />
            </div>
        </div>
    )
}

export default Contact