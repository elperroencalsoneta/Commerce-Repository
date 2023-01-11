

const SearchBox = ({
    categories,
    search,
    onChange,
    onSubmit,
}) => {
    return (
        <form onSubmit={e => onSubmit(e)} className="text-base  font-medium text-yellow-600 hover:text-yellow-500">
            <div>
                <div className="mt-1 flex rounded-md shadow-sm">
                    <div className="relative flex items-stretch flex-grow focus-within:z-10">
                        
                            <div className="mt-1 mx-1 px-2 py-1">
                                <select
                                    onChange={e => onChange(e)}
                                    name='category_id'
                                    // className='rounded-full'
                                    style={{
                                        backgroundColor: 'gray-600',
                                        borderRadius: '25px'
                                    }}
                                >
                                    <option value={0}>All</option>
                                    {
                                        categories && 
                                        categories !== null &&
                                        categories !== undefined &&
                                        categories.map((category, index) => (
                                            <option key={index} value={category.id}>
                                                {category.name}
                                            </option>
                                        ))
                                    }

                                </select>
                            </div>

                        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                        </div>
                        <input
                            type="search"
                            name="search"
                            onChange={e => onChange(e)}
                            value={search}
                            required
                            className="focus:ring-yellow-500 focus:border-gray-500 block w-full  pl-2 sm:text-sm border-gray-300"
                            placeholder="Was möchtest du sehen?"
                        />
                    </div>
                    <button
                        type="submit"
                        className="-ml-px relative inline-flex items-center space-x-2 px-4 py-2 border border-gray-300 text-sm font-medium text-gray-700 bg-gray-50 hover:bg-gray-100 focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500"
                        >
                            {/* SORT ASCENDING ICON */}
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="w-6 h-6">
                            <path fillRule="evenodd" d="M10.5 3.75a6.75 6.75 0 100 13.5 6.75 6.75 0 000-13.5zM2.25 10.5a8.25 8.25 0 1114.59 5.28l4.69 4.69a.75.75 0 11-1.06 1.06l-4.69-4.69A8.25 8.25 0 012.25 10.5z" clipRule="evenodd" />
                        </svg>
                        <span>Suchen</span>
                    </button>
                </div>
            </div>
        </form>
    )
}

export default SearchBox;