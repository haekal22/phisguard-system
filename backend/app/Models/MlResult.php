<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class MlResult extends Model
{
    protected $fillable = [
    'report_id',
    'label',
    'risk_score',
    'priority',
    'reason',
    'url_analysis'
];

    protected $casts = [
        'url_analysis' => 'array',
    ];

   public function report()
{
    return $this->belongsTo(Report::class);
}
}
