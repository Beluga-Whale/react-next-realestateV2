import React from 'react'
import Image from 'next/image'
import Link from 'next/link'

const Country = () => {
    return (
        <div id="country" className='country-contain' >

            <Link href="/CountryAll/AmericaHome/">
                <div className='country-items'>
                    <Image className='duration-700 hover:scale-125' src={'/America.svg'} alt="America" width={278} height={426} />
                    <h1 className='country-h1'>AMERICA</h1>
                </div>
            </Link>

            <Link href="/CountryAll/SpainHome/">
                <div className='country-items'>
                    <Image className='duration-700 hover:scale-125' src={'/Spain.svg'} alt="Spain" width={278} height={426} />
                    <h1 className='country-h1'>SPAIN</h1>
                </div>
            </Link>


            <Link href="/CountryAll/LondonHome/">
                <div className='country-items'>
                    <Image className='duration-700 hover:scale-125' src={'/London.svg'} alt="London" width={278} height={426} />
                    <h1 className='country-h1'>LONDON</h1>
                </div>
            </Link>


            <Link href="/CountryAll/FranceHome/">
                <div className='country-items'>
                    <Image className='duration-700 hover:scale-125' src={'/France.svg'} alt="France" width={278} height={426} />
                    <h1 className='country-h1'>FRANCE</h1>
                </div>
            </Link>

        </div>
    )
}

export default Country