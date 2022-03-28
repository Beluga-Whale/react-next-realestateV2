import React from 'react'
import Link from 'next/link'

const SideBar = () => {
    return (
        <div>
            <section className="sidebar">
                <Link className='target' href="/CountryAll/AmericaHome/">
                    <a className='target'>America</a>
                </Link>
                <Link className='target' href="/CountryAll/SpainHome/">
                    <a className='target'>Spain</a>
                </Link>
                <Link className='target' href="/CountryAll/LondonHome/">
                    <a className='target'>London</a>
                </Link>
                <Link className='target' href="/CountryAll/FranceHome/">
                    <a className='target'>France</a>
                </Link>
            </section>
        </div>
    )
}

export default SideBar